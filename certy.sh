#!/bin/bash

echo "Please paste in the combined list of CSR details provided by the customer. When "
a=""

while read line
do
 a+="$line "
done < "${1:-/dev/stdin}"
# echo "pan site_certs.get_csr:"${a//$'\n'/}
a=${a//-/\\-}
a=${a//#/}
a=${a/'Common name: '/'common_name='\'}
a=${a/'DNS names: '/'',dns_names=\'}
echo "pan site_certs.get_csr:"$a