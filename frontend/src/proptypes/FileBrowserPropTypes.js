import PropTypes, {instanceOf} from 'prop-types';
import {Cookies} from "react-cookie";

export default {
  cookies: instanceOf(Cookies).isRequired,
  prefix: PropTypes.string.isRequired,
  system: PropTypes.string.isRequired,
  systemDisplayName: PropTypes.string.isRequired,
  history: PropTypes.shape({
    length: PropTypes.number.isRequired,
    location: PropTypes.object.isRequired,
    action: PropTypes.string.isRequired,
  }).isRequired
};