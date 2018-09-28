#!/bin/bash

# Parse CSR input to produce string used to generate CSR
# Inputs: text from pasteboard
# Output: command with arguments
#

echo 'Paste the CSR details provided by the customer';
read CSR_details;


# Clean data 
# Remove any superfluous chars
# Escape any args w/ a comma
# Wrap each arg in quotes
