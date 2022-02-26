import React from 'react';
import {
  MDBFooter,
  MDBContainer,
  MDBCol,
  MDBRow,
  MDBIcon
} from 'mdb-react-ui-kit';
import 'mdb-react-ui-kit/dist/css/mdb.min.css'

import { motion } from "framer-motion";


const FooterVariants = {
  container: {
    initial: {
      opacity: 0,
      y: -50
    },
    animate: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.5,
        ease: [0.6, -0.05, 0.01, 0.99]
      }
    }
  },
  row: {
    initial: {
      opacity: 0,
      y: -50
    },
    animate: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.5,
        ease: [0.6, -0.05, 0.01, 0.99]
      }
    }
  },
  col: {
    initial: {
      opacity: 0,
      y: -50
    },
    animate: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.5,
        ease: [0.6, -0.05, 0.01, 0.99]
      }
    }

  },
  icon: {
    initial: {
      opacity: 0,
      y: -50
    },
    animate: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.5,
        ease: [0.6, -0.05, 0.01, 0.99]
      }
    }
  }
}


export default function FooterView () {
  return (
    <MDBFooter className='text-center text-white mt-8' >
   <motion.div variants={FooterVariants } initial="initial" animate="animate" icon="icon" rows="row" cols="col" className='container p-4 pb-0  space-x-5'  style={{
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
              letterSpacing: ".5rem",
              lineHeight: "1.5rem",
              textShadow: "0px 0px 10px #6f00ff",
              // textTransform: "uppercase",
            }}>
        <section className='mb-4'>
          <a
            className='btn btn-primary btn-floating m-1'
            style={{ backgroundColor: '#3b5998' }}
            href='https://www.facebook.com/parvez.meherab97/'
            role='button'
            target='_blank'
          >
            <MDBIcon fab icon='facebook-f' />
          </a>

          <a
            className='btn btn-primary btn-floating m-1'
            style={{ backgroundColor: '#55acee' }}
            href='#!'
            role='button'
          >
            <MDBIcon fab icon='twitter' />
          </a>

          <a
            className='btn btn-primary btn-floating m-1'
            style={{ backgroundColor: '#dd4b39' }}
            href='#!'
            role='button'
          >
            <MDBIcon fab icon='google' />
          </a>
          <a
            className='btn btn-primary btn-floating m-1'
            style={{ backgroundColor: '#ac2bac' }}
            href='#!'
            role='button'
            target='_blank'
          >
            <MDBIcon fab icon='instagram' />
          </a>

          <a
            className='btn btn-primary btn-floating m-1'
            style={{ backgroundColor: '#0082ca' }}
            href='https://www.linkedin.com/in/md-golam-mahmud-29b83317a/'
            role='button'
            target='_blank'
          >
            <MDBIcon fab icon='linkedin-in' />
          </a>

          <a
            className='btn btn-primary btn-floating m-1'
            style={{ backgroundColor: '#333333' }}
            href='https://github.com/golammahmud'
            role='button'
            target='_blank'
          >
            <MDBIcon fab icon='github' />
          </a>
        </section>
      </motion.div>


    <div className='text-center  p-3' style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' ,color: `hsl(${Math.random() * 360},100%,50%)`}} >
      © 2022 Copyright&&All rights reserved: 
      <a className='font-serif space-x-1' href='https://mdbootstrap.com/' style={{ color: `hsl(${Math.random() * 360},100%,50%)` }}>
         Md.Golam Mahmud
      </a>
    </div>
  </MDBFooter>
  );
}