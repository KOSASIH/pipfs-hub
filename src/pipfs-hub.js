const express = require('express');
const pipfsHub = require('./pipfs-hub');
const piNetwork = require('./pi-network-sdk');
const ipfsClient = require('./ipfs');

const router = express.Router();

router.use('/files', pipfsHub(piNetwork, ipfsClient));

module.exports = router;
