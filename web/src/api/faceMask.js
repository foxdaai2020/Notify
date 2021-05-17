import appserver from "./appserve";

const API_URL = "/places";

const faceMasks = {
  async queryFaceMasks() {
    return await appserver.get(`${API_URL}`);
  }
};

export default faceMasks;
