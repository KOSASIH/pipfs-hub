import * as IPFS from 'ipfs-core';
import * as PiNetwork from '../src/pi-network-sdk';

async function main() {
  const ipfsNode = await IPFS.create();
  const piNetwork = new PiNetwork.PiNetwork('YOUR_PI_NETWORK_API_KEY');

  // Add a file to IPFS
  const fileAdded = await ipfsNode.add({
    path: "hello.txt",
    content: "Hello World 101",
  });

  console.log("Added file:", fileAdded.path, fileAdded.cid);

  // Add the file to Pi Network
  const piFile = await piNetwork.addFile(fileAdded.cid);

  console.log("Added Pi Network file:", piFile);
}

main();
