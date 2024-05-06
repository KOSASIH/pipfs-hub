const IPFS = require('ipfs');

const ipfs = new IPFS({
  repo: './ipfs-repo',
  start: true,
  EXPERIMENTAL: {
    pubsub: true
  }
});

module.exports = ipfs;
