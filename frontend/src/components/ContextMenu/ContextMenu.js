// @flow
import {addModal} from "../../store/ui/modals/Modals";
import {connect} from 'react-redux';
import EventListener from 'react-event-listener';
import React from 'react';
import {startTransfer} from "../../store/transferFiles/TransferFiles";
import {fileActions, fileListActions} from "../../store/files/Files";
import './ContextMenu.scss';
import {getFocusedFilePaths} from "../../store/ui/reducer";
import DownloadLink from './DownloadLink'
import type {FileType} from "../../types/fileTypes";

type Props = {
  focusedFiles: Array<FileType>,
  focusedFilePaths: Array<string>,
  dispatch(any): typeof undefined,
}

type State = {
  visible: boolean
}

class ContextMenu extends React.Component<Props, State> {
  state = {
    visible: false,
  };
  root: HTMLElement | null = null;

  _eventPathContainsClass = (event, className) => {
    return event.path.map(
        (element) => element.className
    ).filter(cn => cn) // Remove undefined values or any other "falsey" values
     .map(
         // Check if the supplied className is found in the element's className property
         (cn) => (typeof cn === 'string') && cn.indexOf(className) !== -1
     ).includes(true);
  };

  _handleContextMenu = (event) => {
    // console.log("context target", event.currentTarget);
    // console.log("event", event);
    // console.log("classDetection", this._eventPathContainsClass(event, "rightClickableFile"));
    if(!this._eventPathContainsClass(event, "rightClickableFile")) {
      return;
    }

    event.preventDefault();

    this.setState({ visible: true });

    if (this.root === null) {
      return
    }

    const clickX = event.clientX;
    const clickY = event.clientY;
    const screenW = window.innerWidth;
    const screenH = window.innerHeight;
    const rootW = this.root.offsetWidth;
    const rootH = this.root.offsetHeight;

    const right = (screenW - clickX) > rootW;
    const left = !right;
    const top = (screenH - clickY) > rootH;
    const bottom = !top;

    if (right) {
      this.root.style.left = `${clickX + 5}px`;
    }

    if (left) {
      this.root.style.left = `${clickX - rootW - 5}px`;
    }

    if (top) {
      this.root.style.top = `${clickY + 5}px`;
    }

    if (bottom) {
      this.root.style.top = `${clickY - rootH - 5}px`;
    }
  };

  _handleClick = (event) => {
    const { visible } = this.state;
    const wasOutside = !(event.target.contains === this.root);

    if (wasOutside && visible) this.setState({ visible: false, });

    return true;
  };

  _handleScroll = () => {
    const { visible } = this.state;

    if (visible) this.setState({ visible: false, });
  };

  delayedRefresh = (path) => {
    // We delay a bit here so that Dropbox has a chance to be consistent.
    // See "Brewers Cap Theorem" - Consistency, Availability, Partition tolerance
    setTimeout(() => {
      this.props.dispatch(fileListActions.pending(path));
    }, 200);
  };

  handleSingleShareFile = (e) => {
    console.log('share');
  };

  handleMultiShareFile = (e) => {
    console.log('share');
  };

  handleTransferFiles = (e) => {
    const {focusedFiles} = this.props;
    this.props.dispatch(addModal({
      modalType: 'transfer',
      files: focusedFiles,
      action: (targetPath) => {
        const transferOrders = focusedFiles.map(
            // Files get no trailing slash (obviously)
            // Directories must get a trailing slash
            file => ({
              fromPath: file.fullPath + (file.type === 'dir' ? '/' : ''),
              toPath: targetPath + file.name + (file.type === 'dir' ? '/' : '')
            })
        );
        this.props.dispatch(
            startTransfer(transferOrders)
        );
      }
    }));
  };

  handleRenameFile = (e) => {
    const file = this.props.focusedFiles[0];
    this.props.dispatch(addModal({
      modalType: 'renameFile',
      fileName: file.name,
      action: (newName) => {
        this.props.dispatch(
            fileActions.renameFile(file, newName)
        );
        this.delayedRefresh(file.fullPath.split('/').slice(0,-1).join('/') + '/')
      }
    }));
  };

  handleMoveFile = (e) => {
    const {focusedFiles} = this.props;
    const currentDirectoryPath = focusedFiles[0]
        .fullPath.split('/').slice(0,-1).join('/') + '/';

    this.props.dispatch(addModal({
      modalType: 'moveCopyFile',
      title: 'Move File' + (focusedFiles.length > 1 ? 's' : ''),
      files: focusedFiles,
      promptVerb: 'move',
      submitText: 'Move Here',
      path: currentDirectoryPath,
      systemName: focusedFiles[0].system,
      action: (newPath) => {
        const newDirectoryPath = [
          ...currentDirectoryPath.split('/').slice(0, 3),
          ...newPath.split('/').slice(1, -1),
          ''
        ].join('/');

        // Copy each file
        Promise.all(
            focusedFiles.map(
                file => {
                  console.log(file, newPath);
                  return fileActions.moveFile(file, newPath + '/' + file.name)
                }
            ).map(
                moveAction => this.props.dispatch(moveAction)
            )
        )

        // ... then refresh each affected directory
        .then(() => {
          this.delayedRefresh(currentDirectoryPath);
          this.delayedRefresh(newDirectoryPath);
        });
      }
    }));
  };

  handleCopyFiles = (e) => {
    const {focusedFiles} = this.props;
    const currentDirectoryPath = focusedFiles[0]
        .fullPath.split('/').slice(0,-1).join('/') + '/';

    this.props.dispatch(addModal({
      modalType: 'moveCopyFile',
      title: 'Copy File' + (focusedFiles.length > 1 ? 's' : ''),
      files: focusedFiles,
      promptVerb: 'copy',
      submitText: 'Copy Here',
      path: currentDirectoryPath,
      systemName: focusedFiles[0].system,
      action: (newPath) => {
        const newDirectoryPath = [
          ...currentDirectoryPath.split('/').slice(0, 3),
          ...newPath.split('/').slice(1, -1),
          ''
        ].join('/');

        // Copy each file
        Promise.all(
            focusedFiles.map(
                file => fileActions.copyFile(file, newPath + file.name)
            ).map(
                copyAction => this.props.dispatch(copyAction)
            )
        )

        // ... then refresh each affected directory
        .then(() => {
          this.delayedRefresh(newDirectoryPath);
        });
      }
    }));
  };

  handleDeleteFiles = (e) => {
    this.props.dispatch(addModal({
      modalType: 'deleteFile',
      files: this.props.focusedFiles,
      action: () => {
        const uniqueDirectories = this.props.focusedFiles.map(
            // Map from files to their directory paths
            file => file.fullPath.split('/').slice(0,-1).join('/') + '/'
        ).filter(
            // Get unique
            (x,i,a) => a.indexOf(x) == i
        );

        // Delete each file
        Promise.all(
            this.props.focusedFiles.map(
                file => fileActions.deleteFile(file)
            ).map(
                deleteAction => this.props.dispatch(deleteAction)
            )
        )

        // ..then refresh each of their containing directories
        .then(() => {
          console.log(uniqueDirectories);
          uniqueDirectories.forEach(
              (directoryPath) => this.delayedRefresh(directoryPath)
          )
        });
      }
    }));
  };

  singleFileContextMenu = () => (
      <React.Fragment>
        <div className="contextMenu--option contextMenu--option__disabled"
             onClick={this.handleSingleShareFile}
        >
          Share (coming soon)
        </div>
        <div className="contextMenu--option"
             onClick={this.handleTransferFiles}
        >
          Transfer
        </div>
        <DownloadLink file={this.props.focusedFiles[0]}
                      disabled={this.props.focusedFiles[0].type === 'dir'}
        >
          Download
        </DownloadLink>
        <div className="contextMenu--option"
             onClick={this.handleRenameFile}
        >
          Rename
        </div>
        <div className="contextMenu--option"
             onClick={this.handleMoveFile}
        >
          Move
        </div>
        <div className="contextMenu--option"
             onClick={this.handleCopyFiles}
        >
          Copy
        </div>
        <div className="contextMenu--option"
             onClick={this.handleDeleteFiles}
        >
          Delete
        </div>
      </React.Fragment>
  );

  multipleFileContextMenu = () => (
      <React.Fragment>
        <div className="contextMenu--option contextMenu--option__diabled"
             onClick={this.handleMultiShareFile}
        >
          Share (coming soon)
        </div>
        <div className="contextMenu--option"
             onClick={this.handleTransferFiles}
        >
          Transfer
        </div>
        <DownloadLink file={this.props.focusedFiles[0]}
                      disabled={true}
        >
          Download
        </DownloadLink>
        <div className="contextMenu--option"
             onClick={this.handleMoveFile}
        >
          Move
        </div>
        <div className="contextMenu--option"
             onClick={this.handleCopyFiles}
        >
          Copy
        </div>
        <div className="contextMenu--option"
             onClick={this.handleDeleteFiles}
        >
          Delete
        </div>
      </React.Fragment>
  );

  render() {
    const { visible } = this.state;

    return (
        <div>
          <EventListener
              target="window"
              onScroll={this._handleScroll}
              onClick={this._handleClick}
              onContextMenu={this._handleContextMenu}
          >
            {(visible || null) && (
                <div ref={ref => {this.root = ref}}
                     className="contextMenu"
                >
                  {this.props.focusedFilePaths.length === 1 ? this.singleFileContextMenu() : this.multipleFileContextMenu()}
                </div>
            )}
          </EventListener>
        </div>
    );
  };
}

const mapStateToProps = (store) => {
  return {
    focusedFilePaths: getFocusedFilePaths(store),
    focusedFiles: getFocusedFilePaths(store).map(f => store.filesFlat[f])
  };
};

export default connect(mapStateToProps)(ContextMenu);