import React, { useState, useEffect } from "react";

import {
  MDBBtn,
  MDBModal,
  MDBModalDialog,
  MDBModalContent,
  MDBModalHeader,
  MDBModalTitle,
  MDBModalBody,
  MDBModalFooter,
} from "mdb-react-ui-kit";

import ModalView from "./modal";
import ProjectCard from "./projectcard";
import { Button, Modal } from "react-bootstrap";

function CardView({ images, thumbnile, title, description, onClick }) {
  const [lgShow, setLgShow] = useState(false);

  const handleClose = () => setLgShow(false);

  const handleShow = () => setLgShow(true);

  return (
    <div className="sm:mx-auto ml-auto pl-auto">
      <div className="flex flex-wrap justify-center">
        <div className="w-full lg:w-1/2 p-3" onClick={handleShow}>
          <ProjectCard
            title={title}
            description={description}
            image={thumbnile}
          />
        </div>
      </div>

      <Modal
        size="lg"
        show={lgShow}
        onHide={() => setLgShow(false)}
        aria-labelledby="example-modal-sizes-title-lg"
      >
        <Modal.Header closeButton>
          <Modal.Title id="example-modal-sizes-title-lg" >
            {title}
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <ModalView image={thumbnile}/>

          <hr/>
          <article>{description}</article>

        </Modal.Body>
      </Modal>
    </div>
  );
}

export default CardView;

{
  /* <div className="sm:mx-auto ml-auto pl-auto">
<MDBCard style={{ maxWidth: "22rem" }} className="content-between space-x-2">
  <MDBRipple
    rippleColor="light"
    rippleTag="div"
    className="bg-image hover-overlay"
  >
    <MDBCardImage
      src="https://mdbootstrap.com/img/new/standard/nature/111.webp"
      fluid
      alt="..."
    />
    <a>
      <div
        className="mask"
        style={{ backgroundColor: "rgba(251, 251, 251, 0.15)" }}
      ></div>
    </a>
  </MDBRipple>
  <MDBCardBody>
    <MDBCardTitle>Card title</MDBCardTitle>
    <MDBCardText>
      Some quick example text to build on the card title and make up
      the bulk of the card's content.
    </MDBCardText>
    <MDBBtn href="#">Button</MDBBtn>
  </MDBCardBody>
</MDBCard>
<button onClick={() => setIsFlipped(true)}>Click to flip</button>
</div> */
}
