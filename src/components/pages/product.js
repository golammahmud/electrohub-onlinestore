import React from "react";
import { Button, Card,Img,Body } from "react-bootstrap";
import Ruhanika from "../images/ruhanika.jpg";
import { motion, AnimatePresence } from "framer-motion";

const containerVariants = {
  hidden: {
    opacity: 0,
  },
  visible: {
    opacity: 1,
    transition: {
      delay: 0.5,
      duration: 0.5,
      ease: "easeInOut",
    },
  },
};

const cardVariants = {
  hidden: {
    opacity: 0,
    x: "-100vw",
  },
  visible: {
    opacity: 1,
    x: 0,
    transition: {
      type: "spring",
      mass: 0.5,
      delay: 0.5,
      stiffness: 50,
      // duration: 0.8,
      damping: 8,
      when: "beforeChildren",
      staggerchildren: 0.2,
    },
  },
  hover: {
    scale: 1,

    transition: {
      type: "spring",
      mass: 0.5,
      delay: 0.5,
      stiffness: 50,
      // duration: 0.8,
      damping: 8,
      when: "beforeChildren",
      staggerchildren: 0.2,
    },
  },
  tap: {
    scale: 0.7,

    transition: {
      type: "spring",
      mass: 0.5,
      delay: 0.5,
      stiffness: 50,
      // duration: 0.8,
      damping: 8,
      when: "beforeChildren",
      staggerchildren: 0.2,
    },
  },

  exit: {
    x: "-100vw",
    transition: {
      type: "spring",
      stiffness: 50,
      damping: 100,
    },
  },
};
const CardDivVariants = {
  hidden: {
    opacity: 0,
    y: "-100vh",
  },
  visible: {
    opacity: 1,
    x: 0,
    y: 0,
    transition: {
      type: "spring",
      delay: 0.5,
      stiffness: 50,
      damping: 10,
      when: "beforeChildren",
      staggerchildren: 0.2,
    },
  },
  hover: {
    shadow: "lg",
    boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.5)",
    scale: 1.1,
    zIndex: 10,
    x: 2,
    y: 5,
    skewX: 2,
    skewY: 2,

    originX: 0,
    originY: 0,
    position: "relative",
    // rotate: -10,
    boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.5)",
    transition: {
      type: "spring",
      stiffness: 50,
      damping: 10,
      ease: "easeInOut",
      mass: 0.5,
      duration: 0.8,
      staggerchildren: 0.2,
      when: "beforeChildren",
    },
  },
  image: {
    hover: {
      scale: 0.9,
      zIndex: 6,
      x: 2,
      y: 3,
      skewX: 3,
      skewY: -3,

      originX: 0,
      originY: 0,
      position: "relative",
      // rotate: -10,
      boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.5)",
      transition: {
        type: "spring",
        stiffness: 50,
        damping: 10,
        ease: "easeInOut",
        mass: 0.5,
        duration: 0.8,
        staggerchildren: 0.2,
        when: "beforeChildren",
      },
    },
  },
  tap: {
    scale: 1.1,
    zIndex: 10,

    originX: 0,
    originY: 0,
    position: "relative",
    // rotate: -10,
    boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.5)",
    transition: {
      type: "spring",
      stiffness: 50,
      damping: 10,
      ease: "easeInOut",
      mass: 0.5,
      duration: 0.8,
      staggerchildren: 0.2,
      when: "beforeChildren",
    },
  },
  exit: {
    opacity: 0,
    y: "-100vh",
    transition: {
      type: "spring",
      stiffness: 50,
      damping: 10,
    },
  },
};

const cardBoxVariants = {
  hidden: {
    opacity: 0,
    y: "-100vh",
  },
  visible: {
    opacity: 1,
    y: 0,
  
    transition: {
      type: "spring",
      delay: 0.5,
      stiffness: 50,
      damping: 10,
    },
  },
  hover: {
    scale: 1.1,
    zIndex: 10,
    originX: 0,
    originY: 0,

    transition: {
      type: "spring",
      stiffness: 50,
      damping: 2,
      ease: "easeInOut",
      mass: 0.5,
    },
  },
};
function Product() {
  return (
    <motion.div 
    vairants={cardVariants}
    animate="visible"
    initial="hidden"
    
    className="grid gap-4 space-y-7 grid-cols-4 xs:grid-cols-1 sm:grid-flow-cols-1 tab:grid-flow-cols-2 lg:grid-flow-cols-3  xl:grid-flow-cols-3 2xl:grid-flow-cols-4" variants={containerVariants} initial="hidden" animate="visible">
     
     <motion.Card
        variants={cardBoxVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
        style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>

      <motion.Card
        variants={cardVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
        style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>

      <motion.Card
        variants={cardVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
       style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>

      <motion.Card
        variants={cardVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
       style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>

      <motion.Card
        variants={cardVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
       style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>

      <motion.Card
        variants={cardVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
       style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>

      <motion.Card
        variants={cardVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
       style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>

      <motion.Card
        variants={cardVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
       style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>

      <motion.Card
        variants={cardVariants}
        whileHover="hover"
        whileTap="tap"
        exit="exit"
       style={{ width: "20rem", height: "auto" }}
        className=" bg-gradient-to-r from-purple-500 to-pink-500   outline outline-offset-2 outline-2 outline-white ring-offset-2 ring-4 border-2 border-slate-200 rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
      >
        <motion.div
          variants={CardDivVariants}
          whileHover="hover"
          whileTap="tap"
          // exit="exit"
          className=" rounded-lg mx-auto my-auto mr-auto p-auto   text-center grid justify-center align-center "
        >
          <motion.Img
            variants={CardDivVariants}
            whileHover="hover"
            whileTap="tap"
            animate="image"
            className=" rounded-lg bg-cover bg-clip-padding h-5/6 w-screen"
            variant="top"
            src={Ruhanika}
          />
          <Card.Body className="touch-pan-x text-center justify-center p-4 mt-0">
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </motion.div>
      </motion.Card>
    </motion.div>
  );
}

export default Product;
