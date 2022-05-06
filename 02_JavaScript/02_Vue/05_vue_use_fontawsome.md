### install basic lib
```
npm i --save @fortawesome/fontawesome
npm i --save @fortawesome/vue-fontawesome
npm install --save @fortawesome/fontawesome-svg-core
```

### install style  
```
 npm i --save @fortawesome/fontawesome-free-solid
 npm i --save @fortawesome/fontawesome-free-regular
 npm i --save @fortawesome/fontawesome-free-brands
```

### config
```
import fontawesome from '@fortawesome/fontawesome'
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
import solid from '@fortawesome/fontawesome-free-solid'
import regular from '@fortawesome/fontawesome-free-regular'
import brands from '@fortawesome/fontawesome-free-brands'

fontawesome.library.add(solid)
fontawesome.library.add(regular)
fontawesome.library.add(brands)

Vue.component('font-awesome-icon', FontAwesomeIcon)
```

### error
Can't resolve '@fortawesome/fontawesome-svg-core' in

solution:
```
npm install --save @fortawesome/fontawesome-svg-core
```