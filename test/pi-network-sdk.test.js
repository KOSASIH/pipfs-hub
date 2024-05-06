const PiNetwork = require('../src/pi-network-sdk/pi-network');

describe('Pi Network SDK', () => {
  it('should handle user profile request', async () => {
    const piNetwork = new PiNetwork('test-api-key');
    const mockUserProfile = { username: 'test-user' };

    piNetwork.getUserProfile = jest.fn(() => Promise.resolve(mockUserProfile));

    const userProfile = await piNetwork.getUserProfile();

    expect(piNetwork.getUserProfile).toHaveBeenCalled();
    expect(userProfile).toEqual(mockUserProfile);
  });

  it('should handle file upload request', async () => {
    const piNetwork = new PiNetwork('test-api-key');
    const mockFile = { name: 'test.txt', data: Buffer.from('test file') };
    const mockAddFileResponse = { fileId: '123' };

    piNetwork.addFile = jest.fn(() => Promise.resolve(mockAddFileResponse));

    const fileId = await piNetwork.addFile(mockFile);

    expect(piNetwork.addFile).toHaveBeenCalledWith(mockFile);
    expect(fileId).toEqual(mockAddFileResponse.fileId);
  });

  // Add more test cases for other Pi Network SDK functionality
});
