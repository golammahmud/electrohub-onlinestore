import React from "react";
import ParticalIndex from "../particals/index";
import Index from "./index";
import "../../index.css";
import { Routes, Route, Link, useLocation } from "react-router-dom";
import About from "./about";
import ContactPage from "./contact";
import { motion, AnimatePresence } from "framer-motion";
import ThreeD from "./threed";
import ScrollToTop from "react-scroll-to-top";
import MyComponent from "./scrolltop";
import Product from "./product";
import Components from "./components";
import LayoutView from "../pages/utilities/layout";
import NavbarView from "../nav/navbar";
import Portfolio from "./portfolio";
import FooterView from "./footer";



function Home() {
  const location = useLocation();
  const [isVisible, setIsVisible] = React.useState(false);
  return (
    <div className="bg-green-400"  >
      <ParticalIndex />
      <NavbarView />
      <ScrollToTop
        smooth
        showUnder={160}
        top={10}
      className="scroll-top "
        style={{
          width: "10vh",
          justifyContent: "space",
          padding: "5px",
          marginLeft: "5px",
          justifyItems: "center",
          alignItems: "center",
          // backgroundColor: "red",
          borderRadius: "50%",
          position: "fixed",
          bottom: "20px",
          right: "20px",
          zIndex: "1000",

        }}
        color="#6f00ff"
      />

      <AnimatePresence>
        <Routes location={location} key={location.key}>
          <Route path="/" element={<Index />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<ContactPage />} />
          <Route path="/threed" element={<ThreeD />} />
          <Route path="/filter" element={<MyComponent />} />
          <Route path="/portfolio" element={<Portfolio />} />
          <Route path="/components" element={<Components />} />
          <Route path="/layout" element={<LayoutView />} />

          <Route
            path="*"
            element={
              <h2 className="text-center grid justify-center text-4xl font-extrabold my-40 mb-96">
                Page Not Found
              </h2>
            }
          />
        </Routes>
        <FooterView />
      </AnimatePresence>
    </div>
  );
}

export default Home;
