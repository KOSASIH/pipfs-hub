# Using PiPFS Hub

This guide will walk you through the process of using PiPFS Hub to manage files on both the Pi Network and IPFS.

## Prerequisites

Before you begin, make sure you have completed the following steps:

1. **Install the project**: Follow the instructions in the [installation guide](docs/installation.md) to install PiPFS Hub.
2. **Set up the project**: Follow the instructions in the [usage guide](docs/usage.md) to set up PiPFS Hub.

## Basic Usage

To use PiPFS Hub, you will need to import the `pipfs-hub` module and create a new instance of the `PiPFS` class. Here's an example:

```javascript
1. const { PiPFS } = require('pipfs-hub');
2. 
3. const pipfs = new PiPFS();
```

Once you have created a new instance of the PiPFS class, you can use it to interact with the Pi Network and IPFS.

# Interacting with the Pi Network

To interact with the Pi Network, you can use the pi property of the PiPFS instance. Here's an example:

```javascript
1. const { PiPFS } = require('pipfs-hub');
2. 
3. const pipfs = new PiPFS();
4. 
5. // Add a new file to the Pi Network
6. pipfs.pi.addFile('/path/to/file.txt', 'File contents');
7. 
8. // Retrieve a file from the Pi Network
9. const fileContents = pipfs.pi.getFile('/path/to/file.txt');
10. 
11. // Remove a file from the Pi Network
12. pipfs.pi.removeFile('/path/to/file.txt');
```

# Interacting with IPFS

To interact with IPFS, you can use the ipfs property of the PiPFS instance. Here's an example:

```javascript
1. const { PiPFS } = require('pipfs-hub');
2. 
3. const pipfs = new PiPFS();
4. 
5. // Add a new file to IPFS
6. const cid = pipfs.ipfs.addFile('/path/to/file.txt');
7. 
8. // Retrieve a file from IPFS
9. const fileContents = pipfs.ipfs.getFile(cid);
10. 
11. // Remove a file from IPFS
12. pipfs.ipfs.removeFile(cid);
```

# Pinning CIDs

To keep sensitive content censorship resistant, you can use the pin method of the PiPFS instance to pin CIDs. Here's an example:

```javascript
1. const { PiPFS } = require('pipfs-hub');
2. 
3. const pipfs = new PiPFS();
4. 
5. // Pin a CID
6. pipfs.pin(cid);
7. 
8. // Unpin a CID
9. pipfs.unpin(cid);
```

# Advanced Usage
For more advanced usage, you can use the pi and ipfs properties of the PiPFS instance to access the underlying Pi Network SDK and IPFS JavaScript library. Here's an example:

```javascript
1. const { PiPFS } = require('pipfs-hub');
2. 
3. const pipfs = new PiPFS();
4. 
5. // Use the Pi Network SDK to interact with the Pi Network
6. const piNetwork = pipfs.pi;
7. 
8. // Use the IPFS JavaScript library to interact with IPFS
9. const ipfsLibrary = pipfs.ipfs;
```

# Conclusion

In this guide, you learned how to use PiPFS Hub to manage files on both the Pi Network and IPFS. You also learned how to interact with the Pi Network and IPFS, and how to pin CIDs to keep sensitive content censorship resistant.

For more information, see the [API reference guide](docs/.
