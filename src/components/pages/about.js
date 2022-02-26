import React from "react";
import "../../index.css";
import { motion } from "framer-motion";
import Progressbar from "./utilities/progressbar";
import Experience from "./utilities/experience";
import Parvez from "../images/parvez.jpg";
import Ruhanika from "../images/ruhanika.jpg";
import { Image, Container, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { Routes, Route, Link, useLocation, NavLink } from "react-router-dom";
import { MDBRow, MDBCol } from "mdb-react-ui-kit";

const baseVariants = {
  hidden: {
    opacity: 0,
  },
  visible: {
    opacity: 1,
    transition: {
      delayChildren: 1,
      stiffness: 100,
      delay: 0.5,
      when: "beforeChildren",
      staggerChildren: 0.2,
    },
    exit: {
      x: "100vw",
      transition: { ease: "easeInOut" },
    },
  },
  exit: {
    x: "-100vw",
    transition: { ease: "easeInOut" },
  },
};

const leftVariants = {
  hidden: {
    x: "-100vw",
  },
  visible: {
    x: 0,

    transition: {
      delay: 0.5,
      duration: 0.9,
      ease: "easeInOut",
      stiffness: 50,
      type: "tween",
      bounce: true,
      mass: 0.5,
      damping: 0.5,

      when: "beforeChildren",
      staggerChildren: 0.2,

      // loop: Infinity,
    },
  },
};

const rightVariants = {
  hidden: {
    x: "100vw",
  },
  visible: {
    x: 0,

    transition: {
      delay: 0.5,
      duration: 1,
      ease: "easeInOut",
      stiffness: 50,
      type: "tween",
      bounce: true,
      mass: 0.5,
      damping: 0.5,
      when: "beforeChildren",
      staggerChildren: 0.2,

      // loop: Infinity,
    },
  },
};

function About() {
  const now = 60;
  return (
    <motion.div
      variants={baseVariants}
      initial="hidden"
      animate="visible"
      whileHover="hover"
      exit="exit"
      className="my-8"
      id="about"
    >
      <div className=" text-center font-serif font-bold   justify-center justify-items-center">
        {" "}
        <motion.h1
          initial={{ opacity: 0, y: "-100vh" }}
          animate={{
            opacity: 1,
            y: 0,
            transition: {
              duration: 0.6,
              bounce: true,
              type: "spring",
              stiffness: 150,
            },
          }}
          className="page-title text-center font-serif  justify-center justify-items-center"
        >
          About Me
        </motion.h1>
        <hr className="   text-red-700  justify-center justify-items-center justify-self-center" />
      </div>

     <div className="grid xs:grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2 3xl:grid-cols-1   gap-4">
       
     <motion.div variants={leftVariants} className="xs:col-span-6 my-10 mx-20 ">
              <div
                className="w-56 h-44 xs:w-48 xs:h-40 bg-blue-700  grid  justify-items-center mx-auto xs:mx-auto sm:mx-auto md:mx-auto lg:mx-auto xl:mx-auto 2xl:mx-auto 3xl:mx-auto justify-center align-center z-20 mb-4 bg-image hover-zoom rounded-pill  border-2 border-indigo-300  radious-2 ring-2 ring-red-600 outline outline-white outline-offset-4 ring-offset-white"
                style={{ width: "280px", height: "200px" }}
              >
                <img
                  src={Parvez}
                  // src='https://mdbootstrap.com/img/new/standard/city/047.webp'
                  className=" w-56 h-44  mb-10 img-fluid rounded-pill xs:rounded-pill sm:rounded-pill md:rounded-pill lg:rounded-pill z-50"
                  alt="parvez"
                  style={{ width: "320px", height: "200px" }}
                />
                {/* <Image
              src={Parvez}
              // roundedCircle
              // className='img-fluid rounded'
              className="z-20 align-middle jystify-center mb-4  border-2 border-indigo-300 img-fluid rounded-pill radious-2 ring-2 ring-red-600 outline-white outline-offset-4 ring-offset-white "
              style={{ width: "33vh", height: "33vh" }}
            /> */}
 
              </div>
              <div className=" mt-0">
              <h6 className=" mt-10 header text-center justify-center grid font-serif font-semibold text-xl text-orange-500">
                  Me,MySelf & I
                </h6>
                <p className="text-center text-zinc-600 whitespace-normal text-lg font-serif font-semibold">
                  I'm a Front-End Developer for ChowNow in Los Angeles, CA. I
                  have serious passion for UI effects, animations and creating
                  intuitive, dynamic user experiences.
                </p>
                <h6 className="text-center text-md text-orange-600">
                  <NavLink
                    to="#"
                    style={({ isActive }) => {
                      return {
                        color: isActive ? "#f00" : "#000",
                        textDecoration: "none",
                      };
                    }}
                  >
                    Let's make something special.
                  </NavLink>
                </h6>
              </div>
            </motion.div>
            <motion.div variants={rightVariants}>
              <div className="space-y-2">
                <div className="">
                  <Experience />
                </div>
              </div>
              <h2 className="text-center  font-serif justify-center align-center mt-6">
                My skills
              </h2>
              <div className="justify-between container mx-auto my-8 px-4 ">
                <div>
                  <Progressbar sub="Html 5" done="90" />
                </div>
                <div>
                  <Progressbar sub="CSS" done="85" />
                </div>
                <div>
                  <Progressbar sub="JavaScript" done="70" />
                </div>
                <div>
                  <Progressbar sub="React.Js" done="60" />
                </div>
                <div>
                  <Progressbar sub="Python" done="80" />
                </div>
                <div>
                  <Progressbar sub="Django" done="70" />
                </div>
              </div>
            </motion.div>
       
        
      
      </div>
      {/* <div className="grid grid-cols-2 gap-4 grid-flow-col  xs:grid-cols-1   sm:grid-cols-1 md:grid-cols-1 "> */}
    </motion.div>
  );
}

export default About;

{
  /* <motion.div
initial={{ opacity: 0 }}
animate={{ margonTop: [0, 100, 0, 50], opacity: 1 }}
transition={{ ease: "easeOut", duration: 5, delay: 1.5 }}
className="text-center grid font-serif justify-center  font-extrabold space-y-20"
>
{" "}
<motion.h2
  animate={{
    fontFamily: "Roboto",
    fontSize: "2rem",
    color: "red",
  }}
  transition={{ duration: 3, delay: 1.5, type: "spring", stiffness: 5 }}
  //   className="text-center grid font-serif justify-center  font-extrabold m-y-30"
>
  this is a About
</motion.h2>
<motion.button
  animate={{ scale: 1.5 }}
  className="text-center grid  justify-center  bg-blue-600 text-red-600 font-serif font-bold border-2 rounded-full  outline   outline-slate-400  "
>
  Save Changes
</motion.button>

</motion.div> */
}
