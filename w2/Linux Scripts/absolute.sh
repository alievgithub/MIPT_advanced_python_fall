#!/bin/bash

cd /tmp/
mkdir 'hello world'
cd 'hello world'
touch absolute.txt
echo 'hello world!!' > /tmp/'hello world'/absolute.txt
cat absolute.txt
