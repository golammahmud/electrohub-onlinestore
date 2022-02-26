import React from "react";
import {
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBCardText,
  MDBCardImage,
  MDBBtn,
  MDBRipple,
} from "mdb-react-ui-kit";

export default function ProjectCard({image, title, description, onClick}) {

//  findout length of the description
  const descriptionLength = description.length;
  const descriptionLengthLimit = descriptionLength > 75 ? 75 : descriptionLength;
  const descriptionShort = description.substring(0, descriptionLengthLimit);
  console.log(descriptionShort);
  const descriptionShortLength = descriptionShort.length;
  console.log(descriptionShortLength);
  
  return (
    <MDBCard className=" text-black" style={{}}>
    <MDBCardImage
      src={image}
      alt={title}
      position="top"
    />
    <MDBCardBody>
      <MDBCardTitle>{title}</MDBCardTitle>
      <MDBCardText>
        {descriptionShort}
      </MDBCardText>
    </MDBCardBody>
  </MDBCard>
  );
}
