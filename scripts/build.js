const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Set the build directory
const buildDir = path.join(__dirname, '..', 'build');

// Remove the build directory if it already exists
if (fs.existsSync(buildDir)) {
  execSync(`rm -rf ${buildDir}`);
}

// Create the build directory
fs.mkdirSync(buildDir);

// Copy the production-ready files to the build directory
const appDir = path.join(__dirname, '..', 'src');
const targetDir = path.join(buildDir, 'app');
fs.copyFileSync(path.join(appDir, 'index.html'), path.join(targetDir, 'index.html'));
fs.copyFileSync(path.join(appDir, 'main.js'), path.join(targetDir, 'main.js'));

// Build the project using webpack
execSync('npx webpack --config webpack.prod.config.js');

console.log('Build completed successfully');
