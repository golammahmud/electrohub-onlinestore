import React, { Component } from "react";
import Parvez from "../../images/parvez.jpg";
import Ruhanika from "../../images/ruhanika.jpg";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from "react-responsive-carousel";

function ModalView({image}) {
  return (
    <div>
      <Carousel
        infiniteLoop={true}
        showArrows={true}
        autoPlay={false}
        showThumbs={false}
        showIndicators={false}
        showStatus={false}
        emulateTouch={true}
        showThumbs={false}
        swipeable={true}
        stopOnHover={true}
        interval={2000}
        transitionTime={500}
        thumbWidth= {100}
        swipeScrollTolerance={5}
        centerSlidePercentage = {50}
        dynamicHeight = {false}
        width = {'100%'}
      >
        <div className=" w-auto">
          <img
            src={image}
            className="rounded mx-auto d-block"
            height="250"
            width="250"
          />
          {/* <p className="legend">Legend 1</p> */}
        </div>
        <div className=" w-auto">
          <img
            src={Parvez}
            className="rounded mx-auto d-block"
            height="250"
            width="250"
          />
          {/* <p className="legend">Legend 2</p> */}
        </div>
       
      </Carousel>
    </div>
  );
}

export default ModalView;
