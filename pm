# only change the profile for on charging cable
if [ "$1" == "alwayson" ]
then
  sudo pmset -c sleep 0
  sudo pmset -c disksleep 0
  echo "You'd better have a good reason for this!"
elif [ "$1" == "saving" ]
then
  sudo pmset -c disksleep 15
  sudo pmset -c sleep 20
  echo "Thank you for saving the planet!"
elif [ "$1" == "status" ]
then
  sudo pmset -g | grep -e \* -e 'sleep\s'
else
  echo "RTFC"
fi
