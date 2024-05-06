const pipfsHub = require('../src/pipfs-hub');
const piNetwork = require('../src/pi-network-sdk');
const ipfs = require('../src/ipfs');

jest.mock('../src/pi-network-sdk');
jest.mock('../src/ipfs');

describe('PiPFS Hub', () => {
  afterEach(() => {
    piNetwork.mockClear();
    ipfs.mockClear();
  });

  it('should handle file upload', async () => {
    const mockFile = Buffer.from('test file');
    const mockPiNetworkAddFileResponse = { fileId: '123' };
    const mockIpfsAddResponse = { path: '/ipfs/QmTest' };

    piNetwork.mockImplementation(() => ({
      addFile: jest.fn(() => Promise.resolve(mockPiNetworkAddFileResponse))
    }));

    ipfs.mockImplementation(() => ({
      add: jest.fn(() => Promise.resolve(mockIpfsAddResponse))
    }));

    const req = {
      file: {
        data: mockFile,
        name: 'test.txt',
        mimetype: 'text/plain'
      }
    };

    const res = {
      status: jest.fn(),
      json: jest.fn()
    };

    await pipfsHub()(req, res);

    expect(piNetwork).toHaveBeenCalledWith(req.file);
    expect(ipfs).toHaveBeenCalledWith(mockPiNetworkAddFileResponse.fileId);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({
      fileId: mockPiNetworkAddFileResponse.fileId,
      ipfsPath: mockIpfsAddResponse.path
    });
  });

  // Add more test cases for other PiPFS Hub functionality
});
