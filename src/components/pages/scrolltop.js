import React ,{ useState} from 'react';
import { Link, Button, Element, Events, animateScroll as scroll, scrollSpy, scroller } from 'react-scroll'
import {motion} from "framer-motion";


const MyComponent = () => {
  // const [isHovered, setHovered] = useState(false)

  // Simplified example

  const buttonVariants = {
    hidden: { opacity: 0, x: -100 },
    visible: {
      opacity: 1,
      x: 200,
      y: 100,
      z: 20,
     
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
  function onTap(event, info) {
    console.log(info.point.x, info.point.y)
  }
  
  return (
    <div>
      <Link activeClass="active" to="section1" spy={true} smooth={true} offset={-70} duration={500}>
        <motion.button
          initial="hidden"
          animate="visible"
          whileHover="hover"
          whileTap="tap"
          variants={buttonVariants}
          whileInView={{ opacity: .7 }}
          className="mb-96 bg-blue-500 hover:bg-blue-700  text-white font-bold py-2 px-4 rounded"
        >
          save as
        </motion.button>
      </Link>

      <motion.div drag="x" dragPropagation
  dragTransition={{ bounceStiffness: 600, bounceDamping: 10 }} onTap={onTap} className="mt-96">top
        </motion.div>
     

      </div>
    // <svg>
    //   <image
    //     filter="url(#blur)"
    //     onMouseEnter={() => setHovered(true)}
    //     onMouseLeave={() => setHovered(false)}
    //   />
    //   <filter id="blur">
    //     <motion.div
    //       initial={false}
    //       animate={{ stdDeviation: isHovered ? 0 : 2 }}
    //     />
    //   </filter>
    // </svg>
  )
}

export default MyComponent;