import React from "react";
import { motion, useCycle } from "framer-motion";
const buttonVariants = {
  hidden: { opacity: 0, x: -100 },
  visible: {
    opacity: 1,
    x: 0,
    y: 100,
    transition: {
      type: "spring",
      stiffness: 300,
      damping: 200,
    },
  },
  hover: {
    scale: 1.4,
    color: "red",
    transition: {
      type: "spring",
    },
  },
  tap: {
    scale: 0.7,
    // rotate: 10,
    color: "blue",
    transition: {
      // yoyo: 10,
      type: "spring",
    },
  },
};

const svgVariants = {
  hidden: { opacity: 0, x: -100, rotate: -180 },
  visible: {
    opacity: 1,
    rotate: 0,
    x: 0,
    y: 100,
    transition: {
      type: "spring",
      stiffness: 300,
      damping: 200,
    },
  },
  hover: {
    scale: 1.4,
    color: "red",
    transition: {
      type: "spring",
    },
  },
  tap: {
    scale: 0.7,
    // rotate: 10,
    color: "blue",
    transition: {
      // yoyo: 10,
      type: "spring",
    },
  },
};

const pathVariants = {
  hidden: { opacity: 0, pathLength: 0 },
  visible: {
    opacity: 1,
    color: "white",
    pathLength: 1,
    transition: {
      type: "spring",
      duration: 4,
      ease: "easeInOut",
    },
  },
};

const loadVariants = {
  animationOne: {
    x: [-20, 20],
    y: [0, -30],
    transition: {
      x: {
        yoyo: Infinity,
        duration: 0.5,
        mass: 0.5,
        damping: 0.2,
        stiffness: 100,
        ease: "easeInOut",
      },
      y: {
        mass: 0.5,
        damping: 0.2,
        stiffness: 100,
        yoyo: Infinity,
        duration: 0.25,
        ease: "easeInOut",
      },
    },
  },
  animationTwo: {
    x: [0],
    y: [0, -60],
    transition: {
      y: {
        yoyo: Infinity,
        duration: 0.25,
        ease: "easeOut",
      },
    },
  },
};
function ThreeD() {
  const [animation, cycleAnimation] = useCycle("animationOne", "animationTwo");
  return (
    <div className="container text-3xl text-center">
      <motion.button
      drag
      dragConstraints={{ left: 0, right: 0, top: 100, bottom: 0 }}
      dragElastic={0.5}
        variants={buttonVariants}
        animate="visible"
        initial="hidden"
        whileTap="tap"
        whileHover="hover"
        onHoverStart={() => console.log("Hover starts")}
        onHoverEnd={() => console.log("Hover ends")}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded p-2"
      >
        save as
      </motion.button>

      <div>
        <motion.svg
          variants={svgVariants}
          animate="visible"
          initial="hidden"
          whileTap="tap"
          whileHover="hover"
          onHoverStart={() => console.log("Hover starts")}
          onHoverEnd={() => console.log("Hover ends")}
          height="210"
          width="400"
        >
          <motion.path
            variants={pathVariants}
            d="M150 0 L75 200 L225 200 Z"
            stroke="black"
            fill="transparent"
          />
        </motion.svg>
        <motion.input whileFocus={{ scale: 1.9}} />

      </div>
      <motion.div
        variants={loadVariants}
        animate={"animationOne"}
        // animate={animation}
        className="w-10 h-10 mx-80 my-auto border rounded-full justify-center align-center bg-yellow-700"
      >
       
      </motion.div>
      {/* <div className="flex justify-center" onClick={() => cycleAnimation()}
      >cycleAnimation
      </div> */}
    </div>
  );
}

export default ThreeD;
