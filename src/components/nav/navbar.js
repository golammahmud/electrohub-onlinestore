import React from "react";
import {
  Navbar,
  FormControl,
  NavDropdown,
  Offcanvas,
  Nav,
  Button,
  Form,
  Container,
  Badge,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { motion } from "framer-motion";
import * as icon from "react-icons/fc";
import * as bicon from "react-icons/fa";
import * as bsicon from "react-icons/bs";
import { Routes, Route, Link, useLocation, NavLink } from "react-router-dom";

const brandVariants = {
  hidden: {
    opacity: 0,
    x: "-100vw",
  },
  visible: {
    opacity: 1,
    x: 0,
    transition: {
      duration: 1,
      ease: "easeInOut",
    },
  },
  hover: {
    scale: 1,
    skewY: 3,
    rotate: 180,
    color: "red",

    transition: {
      duration: 0.5,
      ease: "easeInOut",
    },
  },
};

const nameVariants = {
  hidden: {
    opacity: 0,
    x: "-100vw",
  },
  visible: {
    opacity: 1,
    x: "100vw",
    y: "05vh",
    z: 10,

    skewY: 10,
    skewX: 0,
    rotate: 0,
    scale: 1,


    transition: {
      duration: 1,
      ease: "easeInOut",
    },
  },
  hover: {
    scale: 1.2,
    color: "red",
    skewY: 10,
    skewX: 0,
    rotate: 10,
    fontSize: "2rem",

 

    transition: {
      duration: 0.5,
      ease: "easeInOut",
    },
  },
};

function NavbarView() {
  const name = "GM";
  return (
    <div>
      <Navbar  expand="md" bg="dark" variant="dark">
        <Container fluid>
          <motion.Brand
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              // height: "100%",
              // width: "100%",
              fontSize: "2.5rem",
              fontWeight: "bold",
              color: "#6f00ff",
              textDecoration: "none",
              textAlign: "center",
              fontFamily: "monospace",
              fontStyle: "italic",
              // letterSpacing: ".5rem",
              lineHeight: "1.5rem",
             
              textShadow: "0px 0px 10px #6f00ff",
              textTransform: "uppercase",
            }}
          >
            <h1>
              {name.split("").map((letter, index) => (
                <motion.span
                  key={index}
                  variants={brandVariants}
                  initial="hidden"
                  animate="visible"
                  // whileHover="hover"
                  style={{ color: `hsl(${Math.random() * 360},100%,50%)` }}
                >
                  <NavLink
                    style={({ isActive }) => {
                      return {
                        textShadow: isActive
                          ? "0px 0px 10px #6f00ff"
                          : "0px 0px 10px #fff",
                        boxShadow: isActive
                          ? "0px 0px 10px #6f00ff"
                          : "0px 0px 10px #fff",
                        color: isActive
                          ? "red"
                          : `hsl(${Math.random() * 360},100%,50%)`,
                        fontWeight: "bold",
                        fontSize: "2.5rem",
                        fontFamily: "Times New Roman",
                        textDecoration: "none",
                        borderRadius: isActive ? "2px" : "0px",
                        // border:isActive?"1px solid red":"0px solid red",
                        padding: isActive ? "6px" : "0px",
                      };
                    }}
                    to="/"
                  >
                    <motion.span   >
                      {" "}
                      {letter}
                    </motion.span>
                  </NavLink>
                </motion.span>
              ))}
            </h1>
          </motion.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav">
            {" "}
            <bicon.FaBars color="white" />{" "}
            
          </Navbar.Toggle>
          <Navbar.Collapse id="responsive-navbar-nav" className="navbar-collaps justify-content-end text-white ">
            <Nav
              className="nav-cls justify-content-space-between lg:space-x-8 xl:space-x-8 2xl:space-x-8 3xl:space-x-8" size="large"  
              // style={{ maxHeight: "100px" }}
              // navbarScroll
            >
              
                <NavLink
                  style={({ isActive }) => {
                    return {
                      // textShadow: isActive?"0px 0px 10px #6f00ff":"0px 0px 10px #fff",
                      boxShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        : "none",
                      color: isActive
                        ? "red"
                        : `hsl(${Math.random() * 360},100%,50%)`,
                      fontWeight: "bold",
                      fontSize: "1.4rem",
                      fontFamily: "Times New Roman",
                      textDecoration: "none",
                      borderRadius: isActive ? "2px" : "0px",
                      // border:isActive?"1px solid red":"0px solid red",
                      padding: isActive ? "6px" : "0px",
                    };
                  }}
                  to="/"
                >
                  Home
                </NavLink>
              
   
                <NavLink
                  style={({ isActive }) => {
                    return {
                      textShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        : "0px 0px 10px #fff",
                      boxShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        // : "0px 0px 10px #fff",
                        : "none",
                      color: isActive
                        ? "red"
                        : `hsl(${Math.random() * 360},100%,50%)`,
                      fontWeight: "bold",
                      fontSize: "1.4rem",
                      fontFamily: "Times New Roman",
                      textDecoration: "none",
                      borderRadius: isActive ? "2px" : "0px",
                      // border:isActive?"1px solid red":"0px solid red",
                      padding: isActive ? "6px" : "0px",
                    };
                  }}
                  to="/about"
                >
                  About
                </NavLink>
              

           
                <NavLink
                  style={({ isActive }) => {
                    return {
                      textShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        : "0px 0px 10px #fff",
                      boxShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        : "none",
                      color: isActive
                        ? "red"
                        : `hsl(${Math.random() * 360},100%,50%)`,
                      fontWeight: "bold",
                      fontSize: "1.4rem",
                      fontFamily: "Times New Roman",
                      textDecoration: "none",
                      borderRadius: isActive ? "2px" : "0px",
                      // border:isActive?"1px solid red":"0px solid red",
                      padding: isActive ? "6px" : "0px",
                    };
                  }}
                  to="/portfolio"
                >
                  Portfolio
                </NavLink>
             
                <NavLink
                  style={({ isActive }) => {
                    return {
                      textShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        : "0px 0px 10px #fff",
                      boxShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        : "none",
                      color: isActive
                        ? "red"
                        : `hsl(${Math.random() * 360},100%,50%)`,
                      fontWeight: "bold",
                      fontSize: "1.4rem",
                      fontFamily: "Times New Roman",
                      textDecoration: "none",
                      borderRadius: isActive ? "2px" : "0px",
                      // border:isActive?"1px solid red":"0px solid red",
                      padding: isActive ? "6px" : "0px",
                    };
                  }}
                  to="/contact"
                >
                  Contact
                </NavLink>
              
                <NavLink
                  style={({ isActive }) => {
                    return {
                      textShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        : "0px 0px 10px #fff",
                      boxShadow: isActive
                        ? "0px 0px 10px #6f00ff"
                        : "none",
                      color: isActive
                        ? "red"
                        : `hsl(${Math.random() * 360},100%,50%)`,
                      fontWeight: "bold",
                      fontSize: "1.4rem",
                      fontFamily: "Times New Roman",
                      textDecoration: "none",
                      borderRadius: isActive ? "2px" : "0px",
                      // border:isActive?"1px solid red":"0px solid red",
                      padding: isActive ? "6px" : "0px",
                    };
                  }}
                  to="/blog"
                >
                  Blog
                </NavLink>
             
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </div>
  );
}

export default NavbarView;

// {name.split("").map((letter, index) => (
//   <motion.span
//     key={index}
//     className="letter"
//     style={{ color: `hsl(${Math.random() * 360},100%,50%)` }}
//   >
//     {letter}
//   </motion.span>
// ))}
// <motion.NavLink
//   variants={brandVariants}
//   initial="hidden"
//   animate="visible"
//   whileHover="hover"
//   className="text-blue-600 ml-auto"
//   style={({ isActive }) => {
//     return {
//       color: isActive
//         ? "red"
//         : `hsl(${Math.random() * 360},100%,50%)`,
//       fontWeight: "bold",
//       fontSize: "2.5rem",
//       fontFamily: "Times New Roman",
//       textDecoration: "none",
//     };
//   }}
//   to="/"
// ></motion.NavLink>
