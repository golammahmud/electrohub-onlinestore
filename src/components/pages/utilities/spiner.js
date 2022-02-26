import React from 'react';
import { MDBSpinner } from 'mdb-react-ui-kit';

export default function Spiner() {
  return (
    <MDBSpinner className='mx-2' color='secondary'>
        <span className='visually-hidden'>Loading...</span>
      </MDBSpinner>
  );
}