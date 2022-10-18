#! /bin/bash
#Ensure the script is being run from its directory
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

cd $DIR

echo $(pwd)

#Any process, parent or child, that finishes with an exit 1 code will trigger the err trap:
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

set -E -u -o pipefail -e

echo "Helloworld"
echo "Sleeping $BASH_SLEEP"
sleep $BASH_SLEEP
echo "Done sleeping $BASH_SLEEP"