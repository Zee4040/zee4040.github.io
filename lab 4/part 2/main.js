const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const imageFilenames = ['pic1.jpg','pic2.jpg','pic3.jpg','pic4.jpg','pic5.jpg',]

/* Declaring the alternative text for each image file */
const imageAlts = {
    'pic1.jpg': 'Closeup of a human eye',
    'pic2.jpg': 'Rock that looks like a wave',
    'pic3.jpg': 'Purple and white pansies',
    'pic4.jpg': 'Section of wall from a pharaoh\'s tomb',
    'pic5.jpg': 'Large moth on a leaf'
  };
/* Looping through images */

for (let i = 0; i < imageFilenames.length; i++) {
  const fileName = imageFilenames[i];
  const newImage = document.createElement('img');
  newImage.setAttribute('src', 'images/' + fileName);
  newImage.setAttribute('alt', imageAlts[fileName]);
  thumbBar.appendChild(newImage);
}

/* Wiring up the Darken/Lighten button */
