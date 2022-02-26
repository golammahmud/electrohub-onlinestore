import React, { useState, useEffect, useContext } from "react";
import "../../index.css";
import { motion } from "framer-motion";
import { Routes, Route, Link, useLocation, NavLink } from "react-router-dom";
import Parvez from "../images/parvez.jpg";
import Web from "../images/7.jpeg";
import { Image } from "react-bootstrap";

import {
  homeContext,
  aboutContext,
  portfolioContext,
  contactContext,
  loadContext,
} from "../context/mycontext";

const baseVariants = {
  hidden: {
    opacity: 0,
    // x: "-100vw",
  },
  visible: {
    opacity: 1,
    // x: 0,
    transition: {
      delay: 0.5,
      duration: 0.5,
      ease: "easeInOut",
    },
  },
  exit: {
    x: "-100vw",
    transition: { ease: "easeInOut" },
  },
};

const spanVariants = {
  hidden: {
    opacity: 0,
    x: "-100vh",
    // y: "-200vh",
  },
  visible: {
    fontFamily: "Helvetica Neue",

    opacity: 1,
    x: 0,
    scale: 1.3,
    transition: {
      stiffness: 150,
      delay: 0.5,
      duration: 0.8,
      ease: "easeInOut",
      bounce: true,
      type: "spring",
      when: "afterChildren",
      staggerChildren: 0.2,
      mass: 0.7,
      damping: 0.7,
    },
  },
  hover: {
    y: [-1, -2, -2.8, 0.9, 0],
    scaleY: [1, 1.3, 0.8, 1, 1.2],
    color: `hsl(${Math.random() * 360},100%,50%)`,
  },
  tap: {
    scale: 1.3,
    color: "#00ff00",
    transition: {
      duration: 0.8,
      type: "spring",
      bounce: true,
      mass: 0.7,
    },
  },
};
const list = {
  hidden: {
    opacity: 0,
    transition: {
      when: "afterChildren",
    },
  },
  visible: {
    opacity: 1,
    transition: {
      When: "beforeChildren",
      staggerChildren: 0.2,
    },
  },
  hover: {
    y: [-1, -2, -2.8, 0.9, 0],
    scaleY: [1, 1.3, 0.8, 1, 1.2],
    color: "red",
  },
};

const item = {
  hidden: {
    opacity: 0,
    x: "-100vh",
    y: 0,
    rotate: 180,
    transition: {
      duration: 0.5,
      ease: "easeInOut",
    },
  },
  visible: {
    opacity: 1,
    rotate: 0,
    x: 0,
    y: [-1, -1.9, -2.7, 1],
    scaleY: [1, 1.3, 0.8, 1],
    transition: {
      stiffness: 150,
      delay: 0.5,
      duration: 0.8,
      ease: "easeInOut",
      // bounce: true,
      // type: "spring",
      when: "afterChildren",
      staggerChildren: 0.2,
      mass: 0.7,
      damping: 0.7,
    },
  },
  hover: {
    y: [-1, -2, -2.8, 0.9, 0],
    scaleY: [1, 1.3, 0.8, 1, 1.2],
    color: "red",
  },
};

const text2Variants = {
  hidden: {
    opacity: 0,
    x: "100vh",
    // y: "-200vh",
  },
  visible: {
    fontFamily: "Helvetica Neue",

    opacity: 1,
    x: 0,

    // y:0,

    scale: 1.3,
    // repeat: Infinity,
    transition: {
      stiffness: 150,
      delay: 0.6,
      duration: 0.9,
      ease: "easeInOut",
      // bounce: true,
      // type: "spring",
      when: "afterChildren",
      staggerChildren: 0.2,
      mass: 0.7,
      damping: 0.7,
    },
  },

  hover: {
    y: [-1, -2, -2.8, 0.9, 0],
    scaleY: [1, 1.3, 0.8, 1, 1.2],
    color: "red",
  },
  tap: {
    scale: 1.3,
    color: "#00ff00",
    transition: {
      // delay: 0.5,
      duration: 0.8,
      ease: "easeInOut",
      // bounce: true,
      // type: "spring",
      when: "afterChildren",
      staggerChildren: 0.2,
      // mass: 0.7,
      // damping: 0.7,
    },
  },
};

const text3variants = {
  hidden: {
    opacity: 0,
    x: "-100vh",
    // y: "-200vh",
  },
  visible: {
    fontFamily: "Helvetica Neue",

    opacity: 1,
    x: 0,
    y: 0,
    scale: 1.3,
    transition: {
      stiffness: 150,
      delay: 0.5,
      duration: 1,
      ease: "easeInOut",
      // bounce: true,
      // type: "spring",
      when: "beforeChildren",
      staggerChildren: 0.2,
      mass: 0.7,
      damping: 0.7,
    },
  },
  hover: {
    y: [-1, -2, -2.8, 0.9, 0],
    scaleY: [1, 1.3, 0.8, 1, 1.2],
    color: "red",
  },
  tap: {
    scale: 1.3,
    color: "#00ff00",
    transition: {
      duration: 0.8,
      // type: "spring",
      // bounce: true,
      // mass: 0.7,
      stiffness: 150,
    },
  },
};
function Index() {
  const [homedata, setHomeData] = useContext(homeContext);

  const [loading, setLoading] = useContext(loadContext);

  console.log(homedata);
  // useEffect(() => {
  //   getData();
  // }, []);

  // const getData = async () => {
  //   try {
  //     const response = await fetch(url1);
  //     const data = await response.json();
  //     setHomeData(data);
  //     setLoading(false);
  //   } catch (error) {
  //     setError(error);
  //   }
  // };

  const text1 = "Hellow My Name Is,";
  const text2 = "Golam Mahmud";
  const text3 = " I'm  a Full Stack Web developer";
  const paragraph=" Creating modern and responsive design for mobile and web";
  return (
    <motion.div
      variants={baseVariants}
      initial="hidden"
      animate="visible"
      className="container-fluid text-center justify-center  mb-10   lg:pb-1    "
      id="home"
    >
      <div className="  text-center justify-center lg:mt-44 lg:mb-52  2xl:my-auto 3xl:my-auto   ">
          {/* <div className="grid justify-center align-center mt-20 bg-image hover-zoom rounded-full" style={{ maxWidth: "16rem" ,maxHeight: "16rem" }}> */}

          <div
            className="mb-3 grid justify-center align-center mt-20 bg-image hover-zoom rounded-full z-20   border-2 radious-2 ring-4 ring-red-600 mx-auto"
            style={{ maxWidth: "15rem", maxHeight: "15rem" }}
          >
            <Image
              src={Parvez}
              className="w-100 z-20 align-middle jystify-center mb-10 "
              alt="parvez"
            />
          </div>
          {/* <Image
             src={Parvez}
             // roundedCircle
 
             
             className=" z-20 align-middle jystify-center mb-10 rounded-full border-2 radious-2 ring-4 ring-red-600 "
             style={{ width: "30vh", height: "30vh" }}
           /> */}
          {/* </div> */}
          <div className=" ">
            <motion.h3
              variants={item}
              initial="hidden"
              animate="visible"
              whileHover="hover"
            >
              {text1.split("").map((letter, index) => (
                <motion.span
                  variants={spanVariants}
                  initial="hidden"
                  animate="visible"
                  whileTap="tap"
                  whileHover="hover"
                  key={index}
                >
                  <motion.span variants={list}>{letter}</motion.span>
                </motion.span>
              ))}
            </motion.h3>
          </div>
          <div className="container-fluid">
            <motion.h1
              variants={text2Variants}
              initial="hidden"
              animate="visible"
              // className="text-center justify-center text-6xl font-serif font-bold w-screen bg-yellow-600"
            >
              {text2.split("").map((letter, index) => (
                <motion.span
                  key={index}
                  variants={spanVariants}
                  initial="hidden"
                  animate="visible"
                  whileHover="hover"
                  whileTap="tap"
                  className="text-center justify-center text-6xl font-serif font-bold w-screen "
                >
                  {letter}
                </motion.span>
              ))}
            </motion.h1>
            <div className="">
              <motion.h3
                variants={text3variants}
                initial="hidden"
                animate="visible"
                whileHover="hover"
                whileTap="tap"
                className=""
              >
                {text3.split("").map((letter, index) => (
                  <span key={index}>{letter}</span>
                ))}
              </motion.h3>
            </div>
           
              {/* <motion.p
                variants={text3variants}
                initial="hidden"
                animate="visible"
                whileHover="hover"
                whileTap="tap"
                className=""
              >
                {paragraph.split("").map((letter, index) => (
                  <span key={index}>{letter}</span>
                ))}
              </motion.p> */}
            
            <p className="p-auto ">
               <motion.p
                // variants={text3variants}
                initial={{ opacity: 0, y: -20 }}
                animate={ { opacity: 1, y: 0,transition: { delay: 1.5, duration: 1, ease: "easeInOut" } } }
                whileHover={{ y: -10 }}
                whileTap={{  y: -10 }}
                className=""
              >
                {paragraph.split("").map((letter, index) => (
                  <span key={index}>{letter}</span>
                ))}
              </motion.p>

              {/* Creating modern and responsive design for mobile and web{" "} */}
            </p>
          </div>
        </div>
      {/* {homedata.map(({ text1, text2, text3, paragraph, image = {} } = item) => (
        
        <div className={loading?"animate-pulse":""}>


        </div>
      ))} */}
    </motion.div>
  );
}

export default Index;

{
  /* <div>
        {" "}
        <motion.h2
          variants={baseVariants}
          initial="hidden"
          animate="visible"
          // initial={{ x: -100, opacity: 0 }}
          // animate={{ x: 100, opacity: 1 }}
          // transition={{ duration: 3 }}
          className="text-4xl text-center mt-40 text-red-600"
        >
          This is a simple particals.js example
        </motion.h2>
      </div>

      <div className="text-xl text-center mt-12 text-blue-600">
        <ul>
          <motion.li
            whileHover={{
              scale: 1.3,
              color: "#00ff00",
              textShadow: "0px 0px 10px #00ff00",
            }}
            whileTap={{ scale: 1.3 }}
            transition={{ type: "spring", stiffness: 300, duration: 1 }}
          >
            Animation
          </motion.li>
          <motion.li
            whileHover={{
              scale: 1.3,
              color: "#00ff00",
              textShadow: "0px 0px 10px #00ff00",
            }}
            whileTap={{ scale: 1.3 }}
            transition={{ type: "spring", stiffness: 300, duration: 1 }}
          >
            Particles
          </motion.li>
          <motion.li
            whileHover={{
              scale: 1.3,
              color: "#00ff00",
              textShadow: "0px 0px 10px #00ff00",
            }}
            whileTap={{ scale: 1.3 }}
            transition={{ type: "spring", stiffness: 300, duration: 1 }}
          >
            Canvas
          </motion.li>
          <motion.li
            whileHover={{
              scale: 1.3,
              color: "#00ff00",
              textShadow: "0px 0px 10px #00ff00",
            }}
            whileTap={{ scale: 1.3 }}
            transition={{ type: "spring", stiffness: 300, duration: 1 }}
          >
            WebGL
          </motion.li>
          <motion.li
            whileHover={{
              scale: 1.3,
              color: "#00ff00",
              textShadow: "0px 0px 10px #00ff00",
            }}
            whileTap={{ scale: 1.3 }}
            transition={{ type: "spring", stiffness: 300, duration: 1 }}
          >
            WebGL2
          </motion.li>
        </ul>
      </div>

      <div className="flex justify-center mt-10">
        <div className="">
          <motion.button
            animate={{}}
            whileHover={{
              scale: 1.2,
              textShadow: "0px 0px 10px #fff",
              boxShadow: "0px 0px 10px #fff",
            }}
            className="text-center text-xl  grid  justify-center  bg-blue-600 text-red-600 font-serif font-bold border-2 rounded-full  outline   outline-slate-400 w-40 "
            type="submit"
          >
            Submit
          </motion.button>
        </div>
      </div>  */
}
