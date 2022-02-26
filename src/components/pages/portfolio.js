import React,{useState,useEffect,useContext} from "react";
import CardView from "../pages/utilities/card";
import  { motion } from "framer-motion";
import {homeContext,aboutContext,portfolioContext,contactContext,loadContext} from "../context/mycontext";

const portfolioVariants = {
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
  },
  exit: {
    x: "-100vw",

    transition: { ease: "easeInOut" },
  },
};

const cardVariants = {
  hidden: {
    y: "100vw",
  },
  visible: {
    y: 0,
    originY: 0,

    transition: {
      stiffness: 50,
      type: "tween",
      bounce: true,
      mass: 0.5,
      damping: 0.5,
      delay: 0.5,
      duration: 0.8,
    },
  },
  hover: {},
};
function Portfolio() {
const [portfoliodata, setPortfolioData]=useContext(portfolioContext);
const [loading, setLoading]=useContext(loadContext);




  return (
    <motion.div
      variants={portfolioVariants}
      initial="hidden"
      animate="visible"
      whileHover="hover"
      exit="exit"
      className="content-between space-x-4 mb-96"
    >
      <h1 className="portfolio-title text-center font-serif  justify-center justify-items-center font-semibold my-8 divide-y-2">
        Portfolio
      </h1>
      <motion.div
        variants={cardVariants}
        className="content-between space-x-2  grid grid-cols-4 gap-2 sm:grid-flow-row xs:grid-cols-1 xs:gap-3
         sm:grid-cols-1 sm:gap-3 md:grid-cols-2 md:gap-3 lg:grid-cols-3 lg:gap-3 2xl:grid-cols-4 2xl:gap-3 3xl:grid-cols-4 3xl:gap-3
        
        xs:mx-auto sm:mx-auto md:mx-auto lg:mx-auto xs:justify-center xs:align-center xs:self-center"
      >
        <CardView
          title="Project Title"
          thumbnile="https://mdbootstrap.com/img/Photos/Others/images/43.jpg"
          description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos."
        />

        {/* <CardView/>
        <CardView/>
        <CardView/>
        <CardView/> */}
      </motion.div>
    </motion.div>
  );
}

export default Portfolio;
