import React from "react";
import Lenevo from "../images/lenevo.jpg";
import { Card, Img, Body, Button } from "react-bootstrap";
import { motion, useMotionValue } from "framer-motion";

const containerVariants = {
  hidden: {
    opacity: 0,
  },
  visible: {
    opacity: 1,
    transition: {
      delay: 0.5,
      duration: 0.5,
      type: "spring",
      mass: 0.5,
      damping: 10,
      stiffness: 100,
    },
  },
};

const cardVariants = {
  hidden: {
    y: "-100vh",
    opacity: 0,
  },
  visible: {
    y: 0,
    opacity: 1,
    transition: {
      // delay: 0.5,
      duration: 0.9,
      type: "spring",
      mass: 0.5,
      damping: 10,
      stiffness: 50,
      staggerChildren: 0.3,
      when: "afterChildren",
    },
  },
  hover: {
    // scaleY:1.2,
    x: "10%",
    y: "10%",
    z: 20,
    boxShadow: "0px 0px 20px rgba(0, 0, 0, 0.5)",
    // background: "rgba(255, 255, 255, 0.5)",

    scale: 1.1,
    skew: (5, 5),
    originX: 0,
    originY: 0,
    transition: {
      duration: 0.8,
      type: "spring",
      mass: 0.5,
      damping: 10,
      stiffness: 50,
      staggerChildren: 0.3,
      when: "AfterChildren",
    },
  },
  tap: {
    scale: 1.1,
    transition: {
      duration: 0.5,
      type: "spring",
      mass: 0.5,
      damping: 10,
      stiffness: 50,
      staggerChildren: 0.3,
      when: "beforeChildren",
    },
  },
};

const card = {
  hidden: {
    y: "-100vh",
    opacity: 0,
  },
  visible: {
    y: 0,
    opacity: 1,
    width: "17rem",
    height: "24rem",
    transition: {
      // delay: 0.5,
      duration: 0.9,
      type: "spring",
      mass: 0.5,
      damping: 10,
      stiffness: 50,
      staggerChildren: 0.3,
      when: "beforeChildren",
    },
  },
  hover: {
    // scaleY:1.2,
    scale: 1.05,
    x: "10%",
    y: "10%",
    z: 10,
    zIndex: 20,
    boxShadow: "4px 4px 4px rgba(0, 0, 0, 0.5)",
    shadowColor: "rgba(0, 0, 0, 0.5)",
    shadowBlur: 20,
    shadowOffsetY: 10,
    shadowOffsetX: 10,
    shadowOpacity: 0.5,
    shadowSpread: -10,
    shadowInner: false,
    shadow: true,
    skewY: 2,
    originX: 0,
    originY: 0,
    transition: {
      duration: 0.5,
      type: "spring",
      mass: 0.5,
      damping: 10,
      stiffness: 50,
      ease: "easeInOut",
      // staggerChildren: 0.1,
      // when: "AfterChildren",
    },

  },
};




function Components() {
  return (
    <motion.div initial="hidden" animate="visible" variants={containerVariants}>
      <motion.h2 className="text-center text-2xl font-bold mt-4">
        This is a components pages
      </motion.h2>

      <motion.Card
        variants={card}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
        style={{width: "18rem", height: "auto" }}
        className="w-full md:w-1/2 lg:w-1/3 xl:w-1/4 bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center mt-5 "
      >
        <motion.div
          variants={card}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className="h-auto rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={card}
            // whileHover="hover"
            // whileTap="tap"
            // animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Lenevo}
          />
          <motion.Body
            variants={card}
            className="flex-wrap h-auto text-center justify-center "
          >
           <Card.Title className="text-xl ">Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button className="mb-4 bg-blue-200 rounded-full border-2  p-2 font-semibold"variant="primary ">Go somewhere</Button>
          </motion.Body>
        </motion.div>
      </motion.Card>

      {/* <motion.div
        
        variants={cardVariants}
        // whileHover="hover"
        // whileTap="tap"
        className="flex justify-center mt-4"
      >
        <motion.Card
        variants={card}
        whileHover="hover"
        whileTap="tap"
          style={{width: "18rem", height: "26rem" }}
          className="w-full md:w-1/2 lg:w-1/3 xl:w-1/4 bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center mt-5 "
        >
          <motion.Img
            variants={card}
           
            variant="top"
            src={Lenevo}
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
          />
          <div>
            <motion.Body
              variants={card}
            
              className="text-center text-lg font-bold text-white mt-4"
            >
              Lenevo
            </motion.Body>
            <motion.Button
              variants={card} 
             
              className="bg-white text-black font-bold py-2 px-4 rounded-full mt-4"
            >
              Buy Now
            </motion.Button>

            
          </div>
        </motion.Card>
      </motion.div> */}
    </motion.div>
  );
}

export default Components;
