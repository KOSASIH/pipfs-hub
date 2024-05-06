const axios = require('axios');

const PI_NETWORK_API_URL = 'https://api.pinetwork.com';

class PiNetwork {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.axiosInstance = axios.create({
      baseURL: PI_NETWORK_API_URL,
      headers: {
        'Authorization': `Bearer ${this.apiKey}`
      }
    });
  }

  async getUserProfile() {
    const response = await this.axiosInstance.get('/user/profile');
    return response.data;
  }

  async addFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    const response = await this.axiosInstance.post('/file/add', formData, {
      headers: {
        ...formData.getHeaders()
      }
    });

    return response.data;
  }

  async getFile(fileId) {
    const response = await this.axiosInstance.get(`/file/get?fileId=${fileId}`);
    return response.data;
  }
}

module.exports = PiNetwork;
