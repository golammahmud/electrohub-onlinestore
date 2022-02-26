import React from "react";

import Particles from "react-tsparticles";
import particleConfig from "../config/particalconfig";

function Particals() {
  const particlesInit = (main) => {
    console.log(main);

    // you can initialize the tsParticles instance (main) here, adding custom shapes or presets
  };

  const particlesLoaded = (container) => {
    console.log(container);
  };

  return (
    <div>
      <Particles
        id="tsparticles"
        init={particlesInit}
        loaded={particlesLoaded}
        options={particleConfig}
      />
    </div>
  );
}

export default Particals;
