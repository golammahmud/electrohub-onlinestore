import React from "react";
import Ruhanika from "../../images/ruhanika.jpg";
import { Image } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
function Experience() {
  return (
    <div className="container container mx-auto">
      <h2 className="text-center  font-serif justify-center align-center ">Experience</h2>

      <div className="container justify-content-lg-between justify-content-center px-4 my-4 mx-auto">
        <div className="grid grid-cols-3 gap-3 ">
          <div class="col-span-1">
            <h5>
              <span className="font-semibold">2019-2020</span>
            </h5>
          </div>
          <div class="col-span-2">
            <p className="text-justify text-gray-800">
              Completed gradution studies at Oxford University of Art and Design
            </p>
          </div>
        </div>
      </div>
      <hr className="mb-8" />
    </div>
  );
}

export default Experience;
