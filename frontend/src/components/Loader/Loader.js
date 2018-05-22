import React, {Component} from "react";
import {PropagateLoader} from 'react-spinners';

import PropTypes from 'prop-types';

import './Loader.css';

export default class Loader extends Component {
  static propTypes = {
    visible: PropTypes.bool.isRequired
  };

  render() {
    return (
        <div
            className="loader"
            style={{display: this.props.visible ? 'block' : 'none'}}>
          <PropagateLoader
              color={'#512888'}
              loading={this.props.visible}
          />
        </div>
    );
  };
}