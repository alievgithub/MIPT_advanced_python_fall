#!/bin/bash

cd ..
mkdir 'hello parent'
cd 'hello parent'
touch parent.txt
echo 'hello parent!!' > ../'hello parent'/parent.txt
cat parent.txt

