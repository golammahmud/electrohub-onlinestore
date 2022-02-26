import React, { useState, useEffect } from "react";
import {
  MDBValidation,
  MDBInput,
  MDBBtn,
  MDBCheckbox,
  MDBRow,
  MDBCol,
} from "mdb-react-ui-kit";
import Iframe from "react-iframe";
import Spiner from "./utilities/spiner";

import {motion , AnimatePresence} from "framer-motion";
 

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
  },
  exit: {
    x: "100vw",
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
      duration: 0.6,
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
      duration: 0.6,
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

function ContactPage() {
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  }, []);

  const [formValue, setFormValue] = useState({
    fname: "",
    lname: "",
    email: "",
    message: "",
    phone: "",
    checkbox: false,
  });

  const onChange = (e: any) => {
    setFormValue({ ...formValue, [e.target.name]: e.target.value });
  };

  return (
    <motion.div variants={baseVariants} initial="hidden" animate="visible" whileHover="hover" exit="exit" className="form-group container lg:mb-96 lg:pb-20 xl:mb-96">
      <h1 className="text-center  my-5">Contact </h1>
      <div  class="grid grid-cols-2 gap-4 xs:grid-cols-1 xs:gap-3 sm:grid-cols-1 sm:gap-3 md:grid-cols-1 md:gap-3 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2 3xl:grid-cols-2">
        {loading ? (
          <Spiner />
        ) : (
          <>
            {" "}

            
            <motion.div variants={leftVariants} className="col-md-6">
            <h3 className="text-center font-serif my-4">Map</h3>
              <Iframe
                url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d58312.165403220955!2d89.21494886440298!3d24.013062425730034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39fe84d98fa5bf3d%3A0xb038902617eb9884!2z4Kaq4Ka-4Kas4Kao4Ka-!5e0!3m2!1sbn!2sbd!4v1645462801028!5m2!1sbn!2sbd"
                // width="450px"
                // height="400px"
                id="myId"
                className="myClassname w-96 h-full xs:h-48 xs:w-48 xs:mx-auto md:h-48 md:w-48 md:mx-auto lg:h-64 lg:w-72 xl:h-64 xl:w-72 "
                display="initial"
                position="relative"
              />
            </motion.div>{" "}
          </>
        )}

        <motion.div variants={rightVariants}>
          <MDBValidation className="row g-3" noValidate>
            <div className="col-md-6">
              <MDBInput
                value={formValue.fname}
                name="fname"
                onChange={onChange}
                id="validationCustom01"
                required
                label="First name"
                validation="Looks good!"
                invalid
              />
            </div>
            <div className="col-md-6">
              <MDBInput
                value={formValue.lname}
                name="lname"
                onChange={onChange}
                id="validationCustom02"
                required
                label="Last name"
                validation="Looks good!"
                invalid
              />
            </div>

            <div className="col-md-6">
              <MDBInput
                value={formValue.email}
                name="email"
                onChange={onChange}
                id="validationCustom05"
                required
                label="email"
                validation="Please provide a valid email address."
                type="email"
                invalid
              />
            </div>
            <div className="col-md-6">
              <MDBInput
                value={formValue.phone}
                name="phone"
                onChange={onChange}
                id="validationCustom05"
                required
                validation="Please provide a valid email address."
                label="Phone number input"
                type="tel"
                invalid
              />
            </div>
            <div className="col-12 mb-3 pb-1">
              <MDBInput
                label="Textarea"
                id="validationTextarea"
                textarea
                placeholder="Required example textarea"
                required
                validation="Please enter a message in the textarea."
                invalid
                textarea
                rows={6}
              />
            </div>

            <div className="col-12">
              <MDBBtn type="submit">Submit form</MDBBtn>
            </div>
          </MDBValidation>
        </motion.div>
      </div>
    </motion.div>
  );
}
export default ContactPage;

// import React, { useState, useEffect } from "react";
// import { motion, AnimatePresence } from "framer-motion";
// import "../../index.css";
// import ScrollTop from './scrolltop';
// const containerVariants = {
//   hidden: {
//     opacity: 0,
//     x: "-100vw",
//   },
//   visible: {
//     opacity: 1,
//     x: 0,

//     transition: {
//       type: "spring",
//       mass: 0.5,
//       delay: 0.5,
//       stiffness: 50,
//       // duration: 0.8,
//       damping: 8,
//       when: "beforeChildren",
//       staggerchildren: 0.2,
//     },
//   },
//   hover: {
//     scale: 1.1,
//     rotate: 10,
//     transition: {
//       type: "spring",
//       mass: 0.5,
//       delay: 0.5,
//       stiffness: 50,
//       // duration: 0.8,
//       damping: 8,
//       when: "beforeChildren",
//       staggerchildren: 0.2,
//     },
//   },
//   exit: {
//     x: "-100vw",
//     transition: {
//       type: "spring",
//       stiffness: 50,
//       damping: 100,
//     },
//   },
// };

// const childVariants = {
//   hidden: {
//     opacity: 0,
//     y: "-100vh",
//   },
//   visible: {
//     opacity: 1,
//     y: 0,
//   },
//   hover: {
//     // scale: [1 ,1.1, 1,1.1, 1,1.1, 1,1.1, 1,1.1, 1],
//     scale: 1.3,
//     textShadow: "0px 0px 10px #fff",
//     boxShadow: "0px 0px 10px #fff",
//     color: "#00ff00",
//     // rotate: 10,
//     cursor: "pointer",
//     transition: {
//       yoyo: Infinity,
//       type: "spring",

//       bounce: 0.25,
//       velocity: 2,
//       mass: 0.5,
//       delay: 0.5,
//       stiffness: 50,
//       // duration: 0.8,
//       damping: 8,
//       when: "beforeChildren",
//       staggerchildren: 0.2,
//       min: 0,
//     max: 100,
//     bounceStiffness: 100,
//     bounceDamping: 100,

//     },
//   },
//   exit: {
//     x: "-100vw",
//     transition: {
//         ease: "easeInOut",
//       type: "spring",
//       stiffness: 50,
//       damping: 100,
//     },
//   },
// };
// function Contact() {
//   const [isHovered, setIsHovered] = useState(false);
//   const [show, setShow] = useState(true); //

//   useEffect(() => {
//     setTimeout(() => {
//       setShow(false);
//     }, 4000);
//   }, []);

//   return (
//     <motion.div
//       variants={containerVariants}
//       initial="hidden"
//       animate="visible"
//       exit="exit"
//       className="grid text-3xl space-y-2 justify-center items-center h-screen w-screen "
//     >

//       <h1> Contact pages</h1>
//       <motion.p variants={childVariants} whileHover="hover">
//         framer motion variants using when methods
//       </motion.p>
//       <motion.div variants={childVariants} exit="exit">
//         <ul className="text-blue-600">
//           <li>this is the first list item</li>
//           <li>this is the first list item</li>
//           <li>this is the first list item</li>
//           <li>this is the first list item</li>
//         </ul>
//       </motion.div>

//     </motion.div>
//   );
// }

// export default Contact;
