import axios from "axios";
import router from '../router.js';

const appserve = axios.create({
  baseURL: "https://findmasks.herokuapp.com",
});
appserve.interceptors.response.use(
  function(response) {
    // Do something with response data
    console.log(response);
    return response;
  },
  function(error) {
    console.log(error);
    router.push('/channel')
    return Promise.reject(error);
  }
);

export default appserve;
