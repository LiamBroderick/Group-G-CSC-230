<template>
  <div class="title-box">
    <div class="welcome-title">
      <h1>Glazer Children's Museum</h1>
    </div>
  </div>

  <div class="section">
    <h2>Who Are We?</h2>
    <div class="content">
      <div class="image">
        <img src="https://assets.simpleviewinc.com/simpleview/image/fetch/q_75/https://assets.simpleviewinc.com/simpleview/image/upload/crm/tampabay/Exterior-3--15ede2385056a36_15f14d9c-5056-a36a-08544a40a6d2276e.jpg" alt="Who Are We Image">
      </div>
      <div class="description">
        <p>Here at Glazer Children’s Museum, we want to build a community that values PLAY as the foundation for the learning and development of children and families across generations!</p>
        <p>Allowing your child to choose how they want to play leads to higher engagement and ultimately more fun!</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Why Is Child Development Important?</h2>
    <div class="content centered-content">
      <div class="image">
        <img src="https://i.pinimg.com/736x/21/21/2f/21212fd23ad5891a86b6caa4c69fa945.jpg" alt="Whole Child Image">
      </div>
      <div class="description">
        <p>There are 5 domains involved regarding children development. The exhibits here at Glazier Children’s Museum are dedicated to focus and enhance these different domains!</p>
        <p>1. Physical - "Motor skills allow children to make purposeful movements and learn the physical characteristics of self and the environment."</p>
        <p>2. Social/Emotional - "Emotional development includes the ability to identify and understand one's own feelings, to accurately read and comprehend emotions in others, to manage strong emotions and their expressions, to control one's own behavior, to develop empathy for others, and to establish and maintain relationships."</p>
        <p>3. Sensory - "The ability to recognize and interpret sensory stimuli serves as the basis for understanding, learning, and knowing a particular action or reaction, which plays a major role in the physical, social-emotional, communication, and cognitive development of a child. "</p>
        <p>4. Cognitive - "Cognition also involves the mental activities of comprehending information and the processes or acquiring, organizing, remembering, and using for problem solving and generalization to novel situations."</p>
        <p>5. Communication - "Communication helps children learn to understand or comprehend their wants and needs."</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Why Is Child Led Play Important?</h2>
    <div class="content">
      <div class="image">
        <img src="https://scchildren.org/wp-content/uploads/Group-of-kids-playing-collage-02-800x0-c-default.jpg" alt="Who Are We Image">
      </div>
      <div class="description">
        <p>jusible kamndi kdop kidm lusnd kdjw.</p>
        <p>la la la so important</p>
      </div>
    </div>
  </div>

  <!-- Circles -->
  <div class="circle left-circle1"></div>
  <div class="circle right-circle1"></div>
  <div class="circle left-circle2"></div>
  <div class="circle right-circle2"></div>
  <div class="circle left-circle3"></div>
  <div class="circle right-circle3"></div>

  <button id="map-button"></button>

</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Homepage",
};
</script>


<style scoped>
/* Style for title box */
.title-box {
  background-color: #874791; /* Purple background color */
  padding: 5px; /* Add padding to create space around the title */
  margin-left: 250px;
  margin-right: 250px;
  margin-top: 5px;
  margin-bottom: 45px;
  height: 50px;
  z-index: 1; /* Increase z-index to ensure it's above other elements */
  border-radius: 30px; /* Round the corners */
  display: flex; /* Use flexbox */
  align-items: center; /* Center items vertically */
  justify-content: center; /* Center items horizontally */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* Add shadow */
  border: 2px solid white; /* Adjust the width as needed */
}

/* Style for Glazier Children's Museum title */
.title-box .welcome-title h1 {
  margin: 0; /* Remove all margins */
  text-align: center;
  font-size: 36px; /* Adjust the font size as needed */
  font-family: Vag;
  color: white; /* Set color to white */
}

.section {
  background-color: white; /* White background color */
  margin-top: 35px; /* Add some margin */
  margin-left: 60px;
  margin-right: 60px;
  padding: 20px; /* Add padding */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5); /* Add shadow */
}

.section h2 {
  color: #874791; /* Purple color for section titles */
  font-size: 26px; /* Adjust font size */
  margin-bottom: 15px; /* Add margin */
  margin-top: 0px;
  font-family: Vag;
}

.content {
  display: flex;
  align-items: flex-start; /* Align items at the start (top) of the container */
}

/* Style for centering the second image*/
.centered-content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
  

.image {
  margin-right: 20px;
}

.image img {
  max-width: 500px;
  max-height: 200px;
}

.description {
  flex: 1;
  font-family: Vag;
}

.description p {
  margin-bottom: 10px;
  font-family: Vag;
  text-align: left;
}


/* Style for circles */
.circle {
  position: fixed;
  width: 350px;
  height: 400px;
  border-radius: 100%;
}

/* Left circle */
.left-circle1 {
  left: -220px;
  top: -200px;
  z-index: -2;
  background-color: #874791;
}

/* Right circle */
.right-circle1 {
  right: -220px;
  top: -200px;
  z-index: -2;
  background-color: #874791;
}

/* Left circle */
.left-circle2 {
  left: -125px;
  top: -220px;
  z-index: -3;
  background-color: #f86fac;
}

/* Right circle */
.right-circle2 {
  right: -125px;
  top: -220px;
  z-index: -3;
  background-color: #f86fac;
}

/* Left circle */
.left-circle3 {
  left: -230px;
  top: -90px;
  z-index: -3;
  background-color: #B6E565;
}

/* Right circle */
.right-circle3 {
  right: -230px;
  top: -90px;
  z-index: -3;
  background-color: #B6E565;
}

/* Style for map button */
#map-button {
    position: absolute;
    top: 20px;
    right: 20px; /* Adjust to the right */
    width: 50px; /* Adjust width */
    height: 50px; /* Adjust height */
    background-image: url('https://visualpharm.com/assets/917/Waypoint%20Map-595b40b75ba036ed117d6dd4.svg'); /* Replace 'map-icon.png' with your map image */
    background-size: cover; /* Make sure the background image covers the button */
    border: none; /* Remove border */
    cursor: pointer; /* Add pointer cursor */
}

</style>
