const { execSync } = require('child_process');

// Run the unit tests and integration tests
execSync('npm run test:unit && npm run test:integration');

console.log('Tests completed successfully');
