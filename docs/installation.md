# Installation Guide

This guide will walk you through the process of installing PiPFS Hub on your system. Before you begin, make sure that you have the following prerequisites installed:

- Node.js (version 14 or higher)
- npm (version 6 or higher)

## Step 1: Clone the Repository

First, clone the PiPFS Hub repository from GitHub:

```
git clone https://github.com/KOSASIH/pipfs-hub.git
```
## Step 2: Install Dependencies

Next, navigate to the PiPFS Hub directory and install the project dependencies:

```
1. cd pipfs-hub
2. npm install
```

## Step 3: Configure the Project

Before you can use PiPFS Hub, you need to configure it with your Pi Network and IPFS credentials. Copy the .env.example file to .env and update the values with your own credentials:

```
1. cp .env.example .env
```
Edit the .env file and update the following values:

PI_NETWORK_API_KEY: Your Pi Network API key.
IPFS_API_KEY: Your IPFS API key.

## Step 4: Start the Project

Finally, start the PiPFS Hub project:

```
1. npm start
```

PiPFS Hub will start and you can access it by opening your web browser and navigating to http://localhost:3000.

```
1. 
2. **usage.md**
3. 
4. ```markdown
5. # Usage Guide
6. 
7. This guide will walk you through the process of using PiPFS Hub to store, share, and manage your files on a decentralized network.
8. 
9. ## Step 1: Upload a File
10. 
11. To upload a file to PiPFS Hub, click the "Upload" button in the top right corner of the interface. Select the file that you want to upload and click "Open". PiPFS Hub will upload the file to the IPFS network and display a link to the file.
12. 
13. ## Step 2: Share a File
14. 
15. To share a file with others, copy the link that was displayed when you uploaded the file. You can share this link with anyone and they will be able to access the file on the IPFS network.
16. 
17. ## Step 3: Manage Your Files
18. 
19. To manage your files, click the "Files" button in the top navigation bar. This will display a list of all the files that you have uploaded to PiPFS Hub. From this interface, you can view the details of each file, delete files, and share files with others.
20. 
21. ## Advanced Features
22. 
23. PiPFS Hub includes several advanced features that you can use to manage your files more effectively. These features include:
24. 
25. - **File versioning**: PiPFS Hub automatically creates a new version of a file every time you upload a new version of the file. This allows you to roll back to a previous version of the file if necessary.
26. - **Access control**: PiPFS Hub allows you to control who can access your files. You can set permissions for individual files or for all files in a folder.
27. - **Metadata management**: PiPFS Hub allows you to add metadata to your files. This metadata can include information such as the file's title, description, and tags.
```

