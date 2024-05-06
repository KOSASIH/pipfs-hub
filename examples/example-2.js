import * as IPFS from 'ipfs-core';
import * as PiNetwork from '../src/pi-network-sdk';

async function main() {
  const ipfsNode = await IPFS.create();
  const piNetwork = new PiNetwork.PiNetwork('YOUR_PI_NETWORK_API_KEY');

  // Add multiple files to IPFS
  const file1 = await ipfsNode.add({
    path: "hello1.txt",
    content: "Hello World 1",
  });

  const file2 = await ipfsNode.add({
    path: "hello2.txt",
    content: "Hello World 2",
  });

  // Add the files to Pi Network
  const piFile1 = await piNetwork.addFile(file1.cid);
  const piFile2 = await piNetwork.addFile(file2.cid);

  console.log("Added Pi Network file 1:", piFile1);
  console.log("Added Pi Network file 2:", piFile2);

  // Get the user profile
  const userProfile = await piNetwork.getUserProfile();

  console.log("User Profile:", userProfile);
}

main();
