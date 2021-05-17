import axios from "axios";

const appserve = axios.create({
  baseURL: 'https://findmasks.herokuapp.com',
});

export default appserve;
