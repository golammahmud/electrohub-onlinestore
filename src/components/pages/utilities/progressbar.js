import React, { useState, useEffect } from "react";
// import ProgressBar from "react-animated-progress-bar";
import { ProgressBar } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { motion } from "framer-motion";

function Progressbar({ done, sub }) {
  const [style, setStyle] = React.useState({});

  useEffect(() => {
    setTimeout(() => {
      const newStyle = {
        opacity: 1,
        width: `${done}%`,
        borderRadius: "30px",

        backgroundColor: `hsl(${Math.random() * 360},100%,50%)`,
      };

      setStyle(newStyle);
    }, 200);
  }, [done]);

  //   const now = 80;
  // const [progress, setProgress] = React.useState(0);

  // useEffect(() => {
  //   const timer = setTimeout(() => {
  //     setProgress(now);
  //   }, 1000);
  //   return () => clearTimeout(timer);
  // }, [now]);

  const randomColor = () => {
    const colors = ["#0099ff", "#00cc99", "#ffcc00", "#ff6600", "#ff0000"];
    return colors[Math.floor(Math.random() * colors.length)];
  };

  return (
    <motion.div>
      <div className=" mt-10" >
        <div className="m-0">
          <p className="text-lg font-serif font-semibold">{sub}</p>
        </div>

        <div className="progress w-60 " style={{height: "20px" ,borderRadius: "20px"}}>
          <div className="progress-done" style={style}>
            {done}%
          </div>
        </div>
      </div>
    </motion.div>
    //   <motion.div  >

    //  <ProgressBar variant="info" className="text-red-300 bg-slate-600"now={progress} label={`${progress}%`} animated={true} />
    //   </motion.div>
  );
}

export default Progressbar;
