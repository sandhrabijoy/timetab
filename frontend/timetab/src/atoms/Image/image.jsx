import React from 'react';
import "./image.css";
import leftimage from '../../images/leftimage.webp';
import rightimage from '../../images/rightimage.jpg';
import Descr from '../Descr/Descr'

const Image = (props) => {
  return (
    <div className={props.className}>  
      <div className="image-container">
        <img src={leftimage} alt="left image" />
        <Descr></Descr>
        <img src={rightimage} alt="right image" />
      </div>
    </div>
  );
}

export default Image;
