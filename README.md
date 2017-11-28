# Camera-control-Sony

This is one of my first projects.
I had a camera that could be controled with a mobile phone through wifi.
I wanted to put the camera on a drone and cotrol it through a rasberry pi and a long range WiFi system

The camera connects to the onboard raspberry and the through a basic TCP (WPA2) client/server on groud I could send formatted JSON messages to control the camera.
The video was relayed with GSTREAMER as separate multicast connection.
