import { flags } from './model/flags.js';  

const flagsDiv = document.getElementById('flags-div');  


flags.forEach(flag => {
  const flagItem = document.createElement('div');
  flagItem.classList.add('flag-item');

  const img = document.createElement('img');
  img.src = flag.image;  
  img.alt = flag.name;

  const flagName = document.createElement('p');
  flagName.textContent = flag.name;

  
  flagItem.appendChild(img);
  flagItem.appendChild(flagName);

  flagsDiv.appendChild(flagItem);
});
