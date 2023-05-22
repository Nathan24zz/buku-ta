import io from "socket.io-client";
import { useEffect, useState } from "react";
import { Buffer } from 'buffer';

const socket = io.connect("http://localhost:5555");

function App() {
  const [state, setState] = useState("");
  const [image, setImage] = useState("");

  useEffect(() => {
    socket.on("image", function (data) {
      var frame = Buffer.from(data, 'base64').toString()
      setImage(frame);
    });
  });

  useEffect(() => {
    console.log(state);
    socket.emit("state", state);
  }, [state]);
}

export default App;
