#!/bin/bash

echo "Please paste in the combined list of CSR details provided by the customer."
a=""

while read line
do
 a+="$line "
done < "${1:-/dev/stdin}"
# echo "pan site_certs.get_csr:"${a//$'\n'/}
a=${a// /,}
echo "pan site_certs.get_csr:"$a

