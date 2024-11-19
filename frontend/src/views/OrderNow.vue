<template>
    <div class="container-fluid">
        <!-- <h2>Order Online</h2> -->
        <div class="row">
            <!-- <div class="col-lg-2 col-md-12 col-sm-12 col-12 p-3">
                <div class="card-new bg-white categories-section  rounded">
                    <h4 class="cart-heading p-2"> Categories</h4>

                    <div>
                       <ul class="list-unstyled categories-list" >
                            <li class="category-item">
                                <div class="category-desscription">
                                    Veg 
                                </div>
                                <div class="order-count">
                                   <p>(5)</p>
                                </div>
                            </li>
                            <li class="category-item active">
                                <div class="category-desscription">
                                    Non-Veg 
                                </div>
                                <div class="order-count">
                                   <p>(20)</p>
                                </div>
                            </li>
                       </ul> 
                    </div>
                </div>
            </div> -->

            <!-- menu items -->
            <div class="col-xxl-10 col-xl-9 col-lg-8 col-md-12 col-sm-12 col-12 p-3">
                <div class="menu-items">
                    <div class="row ">

                        <div class="col-lg-4 col-md-4 col-sm-12 col-12 p-2 pt-0">
                            <div class="outlet-card p-2 ">
                                <div class="col-12">
                                    <label for="inputState" class="form-label">Location</label>
                                    <select id="inputState" class="form-select">
                                    <option selected>Choose Location</option>
                                    <option>...</option>
                                    </select>
                                </div>
                            </div>
                        </div>


                        <div class="col-lg-4 col-md-4 col-sm-12 col-12 p-2 pt-0">
                            <div class="outlet-card p-2">
                                <div class="col-12">
                                    <label for="inputState" class="form-label">Category</label>
                                    <select id="inputState" class="form-select">
                                    <option selected>Choose Category</option>
                                    <option>...</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <!-- <div class="col-lg-4 col-md-6 col-sm-12 col-12 p-2">
                            <div class="outlet-card p-2">
                                <div class="restaurent-img">
                                <img class="" src="../assets/CHDS logo Blk transparent.png"> 
                                </div>
                                <div class="outlet-detail">
                                    <h5> Chi Hun Da Su </h5>
                                    <p> Location </p>
                                </div>
                            </div>
                            
                        </div> -->



                        <div class="col-lg-4 col-md-4 col-sm-12 col-12 p-2 pt-0">
                            <div class="search-filter h-100 p-2 ">
                                <form class="d-flex" role="search">
                                    <button class="btn btn-secondary w-100 text-start" type="button" data-bs-toggle="modal" data-bs-target="#searchdishModal"><i class="fa-solid fa-magnifying-glass"></i> Search Dish</button>
                                </form>
                            </div>
                        </div>

                        
                        
                    </div>

                    <div class="divider-heading">
                        <h3>
                            Our Menu
                        </h3>
                    </div>
                    
                    <div class="row p-0">
                        <div class="col-xxl-4 col-xl-6 col-md-6 col-sm-12 col-12 p-2">
                            <div class="card-item " type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <div class="card-item-food p-3">
                                    <div class="food-item-detail">
                                        <h5> Wine-Marinated Chicken Hearts </h5>
                                        <p class="item-price">  $19-$31 </p>
                                        <p class="item-description">
                                            Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as…
                                        </p>
                                        
                                    </div>
                                    <div class="food-image-n-add-item">
                                        <div class="position-relative">
                                            <img class="" src="../assets/dish-images/Soy Braised Beef Shank.png">
                                            <a href="" class="add-item-action">
                                                Add +
                                            </a>
                                        </div>
                                        
                                    </div>
                                </div>
                            </div>
                            
                        </div>

                        <div class="col-xxl-4 col-xl-6 col-md-6 col-sm-12 col-12 p-2">
                            
                            <div class="card-item ">
                                <div class="card-item-food p-3">
                                    <div class="food-item-detail">
                                        <h5> Wine-Marinated Chicken Hearts </h5>
                                        <p class="item-price">  $19-$31 </p>
                                        <p class="item-description">
                                            Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as…
                                        </p>

                                    </div>
                                    <div class="food-image-n-add-item">
                                        <div class="position-relative">
                                            <img class="" src="../assets/dish-images/Soy Braised Beef Shank.png">
                                            <a href="" class="add-item-action">
                                                Add +
                                            </a>
                                        </div>
                                        
                                    </div>
                                </div>
                            </div>
                            
                        </div>

                        <div class="col-xxl-4 col-xl-6 col-md-6 col-sm-12 col-12 p-2">
                            
                            <div class="card-item ">
                                <div class="card-item-food p-3">
                                    <div class="food-item-detail">
                                        <h5> Wine-Marinated Chicken Hearts </h5>
                                        <p class="item-price">  $19-$31 </p>
                                        <p class="item-description">
                                            Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as…
                                        </p>

                                    </div>
                                    <div class="food-image-n-add-item">
                                        <div class="position-relative">
                                            <img class="" src="../assets/dish-images/Soy Braised Beef Shank.png">
                                            <a href="" class="add-item-action">
                                                Add +
                                            </a>
                                        </div>
                                        
                                    </div>
                                </div>

                               
                            </div>
                            
                        </div>

                        <div class="col-xxl-4 col-xl-6 col-md-6 col-sm-12 col-12 p-2">
                            
                            <div class="card-item ">
                                <div class="card-item-food p-3">
                                    <div class="food-item-detail">
                                        <h5> Wine-Marinated Chicken Hearts </h5>
                                        <p class="item-price">  $19-$31 </p>
                                        <p class="item-description">
                                            Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as…
                                        </p>

                                    </div>
                                    <div class="food-image-n-add-item">
                                        <div class="position-relative">
                                            <img class="" src="../assets/dish-images/Soy Braised Beef Shank.png">
                                            <a href="" class="add-item-action">
                                                Add +
                                            </a>
                                        </div>
                                        
                                    </div>
                                </div>

                               
                            </div>
                            
                        </div>
                    </div>
                    
                </div>
            </div>


            <!-- cart  -->
            <div class="col-xxl-2 col-xl-3 col-lg-4 col-md-12 col-sm-12 col-12 p-2 cart-desktop">
                <div class="bg-white cart-section p-2 rounded ">
                    <div class="pb-3">
                        <div class="outlet-card p-2 mb-4">
                            <div class="restaurent-img">
                                <img class="" src="../assets/CHDS logo Blk transparent.png"> 
                            </div>
                            <div class="outlet-detail">
                                <h5> Chi Hun Da Su </h5>
                                <p> Location </p>
                            </div>
                        </div>

                        <h4 class="cart-heading mb-0"> Your Cart</h4>

                        
                    
                        <!-- <div class="order-type-container">
                            <button type="button" class="btn-active-order"> <span> Delivery </span> <br> <span class="delhivery-time">20 Minutes</span> </button>
                            <button type="button" class="btn-inactive-order">Pick Up</button>
                            <button type="button" class="btn-inactive-order">In Car</button>
                        </div> -->
                    </div>
                    


                    <div>
                       <ul class="list-unstyled orderl-list" >
                            <li class="order-item">
                                <div class="order-desscription">
                                    <p class="item-small-hd">Wine-Marinated Chicken Hearts</p>
                                    
                                    <p class="item-price"><span>4 x $ 189</span> <b style="display: inline-block; font-weight: 500;"> $ 756</b></p>
                                </div>
                                <div class="order-count">
                                    <div class="item-action item-action-cart">
                                            <a href="" class="subtract">
                                                <i class="fa-solid fa-minus"></i>
                                            </a>
                                            <p>20</p>
                                            <a href="" class="add">
                                                <i class="fa-solid fa-plus"></i>
                                            </a>
                                        </div>
                                </div>
                            </li>

                            <li class="order-item">
                                <div class="order-desscription">
                                    <p class="item-small-hd">Wine-Marinated Chicken Hearts</p>
                                    
                                    <p class="item-price"><span>4 x $ 189</span> <b style="display: inline-block; font-weight: 500;"> $ 756</b></p>
                                </div>
                                <div class="order-count">
                                    <div class="item-action item-action-cart">
                                            <a href="" class="subtract">
                                                <i class="fa-solid fa-minus"></i>
                                            </a>
                                            <p>20</p>
                                            <a href="" class="add">
                                                <i class="fa-solid fa-plus"></i>
                                            </a>
                                        </div>
                                </div>
                            </li>

                            <li class="order-item">
                                <div class="order-desscription">
                                    <p class="item-small-hd">Wine-Marinated Chicken Hearts</p>
                                    
                                    <p class="item-price"><span>4 x $ 189</span> <b style="display: inline-block; font-weight: 500;"> $ 756</b></p>
                                </div>
                                <div class="order-count">
                                    <div class="item-action item-action-cart">
                                            <a href="" class="subtract">
                                                <i class="fa-solid fa-minus"></i>
                                            </a>
                                            <p>20</p>
                                            <a href="" class="add">
                                                <i class="fa-solid fa-plus"></i>
                                            </a>
                                        </div>
                                </div>
                            </li>

                            <li class="order-item">
                                <div class="order-desscription">
                                    <p class="item-small-hd">Wine-Marinated Chicken Hearts</p>
                                    
                                    <p class="item-price"><span>4 x $ 189</span> <b style="display: inline-block; font-weight: 500;"> $ 756</b></p>
                                </div>
                                <div class="order-count">
                                    <div class="item-action item-action-cart">
                                            <a href="" class="subtract">
                                                <i class="fa-solid fa-minus"></i>
                                            </a>
                                            <p>20</p>
                                            <a href="" class="add">
                                                <i class="fa-solid fa-plus"></i>
                                            </a>
                                        </div>
                                </div>
                            </li>


                       </ul> 
                    </div>
                    <div>
                        <!-- <div class="final-subtotal">
                            <span>Subtotal </span>
                            <span> $  800.00</span>
                        </div> -->
                        
                        <div class="final-subtotal fw-normal">
                            <span class=" ">You have total 8 items in your cart </span>
                        </div>

                        <button type="button" class="btn btn-primary w-100"> Proceed to Checkout </button>
                    </div>
                    
                </div>
                
            </div>

            
            
        </div>
    </div>


    <!-- cart-button-mobile -->
    <div class="mobile-cart">
        <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="offcanvasExample">
           <div class="view-cart-mobile" >
            <p class="mb-0"> 80 Items</p>
            <p class="mb-0"> View Cart </p>
           </div>
        </button>
    </div>

<!-- item detail popup -->
<div class="modal modal-food-item fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">
     
      <div class="modal-body">
        <div class="item-img mb-3">
            <button type="button" class="btn-close btn-close-modal" data-bs-dismiss="modal" aria-label="Close"></button>
            <img class="mb-3" src="../assets/dish-images/Soy Braised Beef Shank.png">
            
            <div>
                <h5> Wine-Marinated Chicken Hearts</h5>
                <p>
                    Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as a nutritious snack.
                </p>

                <div class="price-text"> <span class="fw-bold">$19-$31 </span> </div>
            </div>
        </div>
        
        <div class="px-3 py-2">
            <h4 class="extra-status"> Meal Size : <span  class="text-status"> Meal Set </span> </h4>
            <div class="meal-category rounded p-3">
                <input type="radio" class="btn-check " name="options" id="option1" autocomplete="off" checked>
                <label class="btn btn-primary" for="option1">Meal Set</label>

                <input type="radio" class="btn-check" name="options" id="option2" autocomplete="off">
                <label class="btn btn-outline-primary" for="option2"> Main Dish (300 g)</label>

                <input type="radio" class="btn-check" name="options" id="option3" autocomplete="off">
                <label class="btn btn-outline-primary" for="option3"> meal 3 (300 g)</label>
            </div>
        </div>

        <div class="px-3 py-2">
            <h4 class="extra-status"> Extra protein : <span class="text-status"> Yes </span> </h4>
            <div class="meal-category rounded p-3">
                <input type="radio" class="btn-check " name="protein" id="proteinoption1" autocomplete="off" checked>
                <label class="btn btn-primary" for="proteinoption1">Yes</label>

                <input type="radio" class="btn-check" name="protein" id="proteinoption2" autocomplete="off">
                <label class="btn btn-outline-primary" for="proteinoption2"> No</label>
            </div>
        </div>

        <div class="px-3 py-2">
            <h4 class="extra-status"> Extra vegetables : <span class="text-status"> Yes </span></h4>
            <div class="meal-category rounded p-3">
                <input type="radio" class="btn-check " name="extraveg" id="extraveg1" autocomplete="off" checked>
                <label class="btn btn-primary" for="extraveg1">Yes</label>

                <input type="radio" class="btn-check" name="extraveg" id="extraveg2" autocomplete="off">
                <label class="btn btn-outline-primary" for="extraveg2"> No</label>
            </div>
        </div>


        <div class="px-3 py-2">
            <h4 class="extra-status"> Extra rice : <span class="text-status"> Yes </span> </h4>
            <div class="meal-category rounded p-3">
                <input type="radio" class="btn-check " name="extrarice" id="extrarice1" autocomplete="off" checked>
                <label class="btn btn-primary" for="extrarice1">Yes</label>

                <input type="radio" class="btn-check" name="extrarice" id="extrarice2" autocomplete="off">
                <label class="btn btn-outline-primary" for="extrarice2"> No</label>
            </div>
        </div>
       

        <div class="px-3 py-2">
            <h4 class="nutrients-facts"> Nutrition Facts – Per Meal Set
                (150g Dish + 150g Vegetables + 150g Rice) </h4>
            <div class="meal-category-table rounded ">
                <table class="table w-100">
                <thead>
                    <tr>
                        <th scope="col">Protein</th>
                        <th scope="col">Carb</th>
                        <th scope="col">Fat</th>
                        <th scope="col">Calories</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td >46 g</td>
                        <td>37 g</td>
                        <td>4.2 g</td>
                        <td>370 Kcal</td>
                    </tr>
                </tbody>
                </table>
            </div>
        </div>


        <div class="px-3 py-2 pb-4 bg-white d-flex justify-content-between align-items-center">
            <div class="item-action item-ippopup-action">
                <a href="" class="subtract">
                    <i class="fa-solid fa-minus"></i>
                </a>
                <p>20</p>
                <a href="" class="add">
                    <i class="fa-solid fa-plus"></i>
                </a>
            </div>

            <button type="button" class="btn btn-primary">Add to Cart</button>
        </div>


        
      </div>
      <!-- <div class="modal-footer">
        <button type="button" class="btn btn-primary">Add to Cart</button>
      </div> -->
    </div>
  </div>
</div>


<!-- item search popup -->
<div class="modal modal-search-dish fade" id="searchdishModal" tabindex="-1" aria-labelledby="searchdishModalLabel" aria-hidden="true">
  <div class="modal-dialog  modal-dialog-scrollable modal-dialog-centered">
    <div class="modal-content">

        <div class="modal-header">
            <h5 class="modal-title">Search Dish</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>


        <div class="modal-body bg-modal-body-color ">

            <div class=" mb-3">
                <input class="form-control me-2" type="search" placeholder="Search Dish" aria-label="Search">
            </div>

            <div class="">
                <div class="divider-heading">
                        <h3>
                            Serach Results
                        </h3>
                    </div>
                <div class="meal-category rounded ">
                    <ul class="list-unstyled search-item-list mb-0">
                        <li class="d-flex align-items-center p-3">
                            <img class="searchitem-dish-image" src="../assets/dish-images/Pickled Veg Chicken Stir-fry.png" > 
                            <p class="searchitem-dish-name mb-0">Wine-Marinated Chicken Hearts</p>
                        </li>

                        <li class="d-flex align-items-center p-3">
                            <img class="searchitem-dish-image" src="../assets/dish-images/Pickled Veg Chicken Stir-fry.png" > 
                            <p class="searchitem-dish-name mb-0">Wine-Marinated Chicken Hearts</p>
                        </li>


                        <li class="d-flex align-items-center p-3">
                            <img class="searchitem-dish-image" src="../assets/dish-images/Pickled Veg Chicken Stir-fry.png" > 
                            <p class="searchitem-dish-name mb-0">Wine-Marinated Chicken Hearts</p>
                        </li>


                        <li class="d-flex align-items-center p-3">
                            <img class="searchitem-dish-image" src="../assets/dish-images/Pickled Veg Chicken Stir-fry.png" > 
                            <p class="searchitem-dish-name mb-0">Wine-Marinated Chicken Hearts</p>
                        </li>

                        <li class="d-flex align-items-center p-3">
                            <img class="searchitem-dish-image" src="../assets/dish-images/Pickled Veg Chicken Stir-fry.png" > 
                            <p class="searchitem-dish-name mb-0">Wine-Marinated Chicken Hearts</p>
                        </li>

                    </ul>
                </div>
            </div>

        </div>
      <!-- <div class="modal-footer">
        <button type="button" class="btn btn-primary">Add to Cart</button>
      </div> -->
    </div>
  </div>
</div>



<!-- item cart mobile popup -->


<div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasExampleLabel">Your Cart</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <div class="bg-white cart-section p-2 rounded ">
        <div class="pb-3">
            <div class="outlet-card p-2 mb-4">
                <div class="restaurent-img">
                    <img class="" src="../assets/CHDS logo Blk transparent.png"> 
                </div>
                <div class="outlet-detail">
                    <h5> Chi Hun Da Su </h5>
                    <p> Location </p>
                </div>
            </div>

            
        
            <!-- <div class="order-type-container">
                <button type="button" class="btn-active-order"> <span> Delivery </span> <br> <span class="delhivery-time">20 Minutes</span> </button>
                <button type="button" class="btn-inactive-order">Pick Up</button>
                <button type="button" class="btn-inactive-order">In Car</button>
            </div> -->
        </div>
        


        <div>
            <ul class="list-unstyled orderl-list" >
                <li class="order-item">
                    <div class="order-desscription">
                        <p class="item-small-hd">Wine-Marinated Chicken Hearts</p>
                        
                        <p class="item-price"><span>4 x $ 189</span> <b style="display: inline-block; font-weight: 500;"> $ 756</b></p>
                    </div>
                    <div class="order-count">
                        <div class="item-action item-action-cart">
                                <a href="" class="subtract">
                                    <i class="fa-solid fa-minus"></i>
                                </a>
                                <p>20</p>
                                <a href="" class="add">
                                    <i class="fa-solid fa-plus"></i>
                                </a>
                            </div>
                    </div>
                </li>

                <li class="order-item">
                    <div class="order-desscription">
                        <p class="item-small-hd">Wine-Marinated Chicken Hearts</p>
                        
                        <p class="item-price"><span>4 x $ 189</span> <b style="display: inline-block; font-weight: 500;"> $ 756</b></p>
                    </div>
                    <div class="order-count">
                        <div class="item-action item-action-cart">
                                <a href="" class="subtract">
                                    <i class="fa-solid fa-minus"></i>
                                </a>
                                <p>20</p>
                                <a href="" class="add">
                                    <i class="fa-solid fa-plus"></i>
                                </a>
                            </div>
                    </div>
                </li>

                <li class="order-item">
                    <div class="order-desscription">
                        <p class="item-small-hd">Wine-Marinated Chicken Hearts</p>
                        
                        <p class="item-price"><span>4 x $ 189</span> <b style="display: inline-block; font-weight: 500;"> $ 756</b></p>
                    </div>
                    <div class="order-count">
                        <div class="item-action item-action-cart">
                                <a href="" class="subtract">
                                    <i class="fa-solid fa-minus"></i>
                                </a>
                                <p>20</p>
                                <a href="" class="add">
                                    <i class="fa-solid fa-plus"></i>
                                </a>
                            </div>
                    </div>
                </li>

                <li class="order-item">
                    <div class="order-desscription">
                        <p class="item-small-hd">Wine-Marinated Chicken Hearts</p>
                        
                        <p class="item-price"><span>4 x $ 189</span> <b style="display: inline-block; font-weight: 500;"> $ 756</b></p>
                    </div>
                    <div class="order-count">
                        <div class="item-action item-action-cart">
                                <a href="" class="subtract">
                                    <i class="fa-solid fa-minus"></i>
                                </a>
                                <p>20</p>
                                <a href="" class="add">
                                    <i class="fa-solid fa-plus"></i>
                                </a>
                            </div>
                    </div>
                </li>


            </ul> 
        </div>
        <div>
            <!-- <div class="final-subtotal">
                <span>Subtotal </span>
                <span> $  800.00</span>
            </div> -->
            
            <div class="final-subtotal fw-normal">
                <span class=" ">You have total 8 items in your cart </span>
            </div>

            <button type="button" class="btn btn-primary w-100"> Proceed to Checkout </button>
        </div>
            
    </div>
  </div>
</div>

</template>

<style>

    :root{
        --body-color: #f1f0f5;
        --divider-color: #e4e4e4;
        --card-heading-color: #333333;
        --card-location-color:#787878;
       
        --darkest-green-bg-color: #576d27;
        --order-background-color: #76923b;
        --light-green-color: #b3c677;
        --dark-brown-color : #944c22;
        --light-brown-colo: #c5886b;
        --lightest-brown-colo: #f7d9ba;

    }

    .outlet-card{
        background-color: white;
        border-radius: 0.5rem;
        display: flex;
        gap: 10px;
    }
    .search-filter{
        background-color: white;
        border-radius: 0.5rem;
        vertical-align: middle;
    }

    .restaurent-img{
       border: 1px solid var(--divider-color);
       border-radius: 4px;
        
    }
    .restaurent-img img{
        width: 66px;
        height: 66px;
        object-fit: cover;
    }

    .outlet-detail h5{
        font-size: 17px;
        margin-bottom: 0;
        color: var(--card-heading-color);
    }
    .outlet-detail p{
        font-size: 15px;
        margin-bottom: 0;
        color: var(--card-location-color);
    }


    .divider-heading{
        border-top: 1px solid var(--divider-color);
        width: 100%;
        height: 5px;
        margin-top: 2.5rem;
        margin-bottom: 2.5rem;
        position: relative;
    }

    .divider-heading h3{
        position: absolute;
        text-transform: uppercase;
        top: -0.75rem;
        left: 50%;
        right: 0;
        color: var(--card-heading-color);
        background-color: var(--body-color) !important;
        width: max-content;
        padding: 0 10px;
        font-size: 20px;
        transform: translate(-50%, 0);
    }


    .card-item {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 8px rgb(0 0 0 / 10%);
    }

    .card-item-food{
        display: flex;
        padding-bottom: 30px !important;
        
    }
    .food-item-detail{
        flex: 0 0 60%;
        padding-right: 0.5rem;
    }

    .food-image-n-add-item{
        flex: 0 0 40%;
    }

    .item-price {
        font-weight: 600;
        font-size: 15px;
        margin-bottom: 8px;
        line-height: 15px;
        cursor: pointer;
    }
    .item-price small{
        color: #848484;
        font-size: 85%;
    }

    .food-item-detail h5{
        font-size: 1rem;
        margin-bottom: 0.5rem;
        color: var(--order-background-color);
    }
    .food-item-detail .item-description{
        font-size: 12px;
        color: var(--card-location-color);
    }


    .food-image-n-add-item{
        position: relative;

    }

    .food-image-n-add-item img{
        width: 100%;
        border-radius: 1rem;
        object-fit: cover;
        
    }

    .add-item-action{
        font-size: 16px;
        font-weight: 600;
        padding: 3px 12px;
        border: 1px solid var(--order-background-color);
        border-radius: 8px;
        width: max-content !important;
        text-align: center;
        position: absolute;
        background-color: white;
        position: absolute;
        bottom: -18px;
        left: 50%;
        transform: translate(-50%, 0%);
        text-decoration: none;
        color: var(--order-background-color)
    }

    .item-action{
        display: flex;
    }

    .item-action{
        position: absolute;
        bottom: -18px;
        left: 50%;
        transform: translate(-50%, 0%);
        color: white;
    }
    .item-action .subtract{
        padding:5px;
        background-color: var(--order-background-color);
        border-top-left-radius: 10px;
        border-bottom-left-radius: 10px;
        color: white;
        text-decoration: none;
        height: 32px;
    }

    .item-action p{
        padding: 5px;
        background-color: var(--order-background-color);
        margin-bottom: 0;
        height: 32px;
        width: 30px;
        text-align: center;
    }
    .item-action .add{
        padding: 5px;
        background-color: var(--order-background-color);
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        color: white;
        text-decoration: none;
        height: 32px;
    }

    .calories-detail{
        margin-top: 10px;
    }
    .calories-detail .overall-cal{
        background-color: #b3c677;
        width: 100%;
        display: block;
        text-align: center;
    }
    

    .ingridients-list{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.5rem 1rem 1rem;
        flex-wrap: wrap;
    }

    .ingridients-list li{
        display: flex;
        align-items: center;
        flex-direction: column;
    }
    .ingridients-list li .nutreents{
        font-weight: 500;
        color: var(--card-location-color);
        font-size: 12px;
    }

    .ingridients-list li span:nth-child(2){
        font-size: 13px;
    }


    .cart-section{
        position: sticky;
        position: -webkit-sticky;
        top: 72px;
        z-index: 1;
        background: #fff;
        padding: 10px 10px;
        border-radius: 10px 10px 0px 0px;
        height: calc(100vh - 88px);
    }

    .categories-section{
        position: sticky;
        position: -webkit-sticky;
        top: 72px;
        z-index: 1;
        background: #fff;
        border-radius: 10px 10px 0px 0px;
        height: calc(100vh - 88px);
        /* border-bottom: 1px solid var(--card-heading-color); */
    }

    /* --------------------cart ---------------- */
    .cart-heading{
        font-weight: 600;
        font-size: 17px;
        margin-bottom: 15px;
        color: var(--card-heading-color)
    }
    .order-type-container{
        display: flex;
        padding: 10px 0;
        border: 1px solid var(--divider-color);
        padding: 4px;
        border-radius: 1rem;
    }

    .btn-active-order{
        background-color: #76923b;
        color: white;
        outline: none;
        padding: 10px 1rem;
        border:none;
        font-size: 12px;
        border-radius: 12px;
        width: 33%;
    }

    .btn-active-order:hover{
        background-color: #76923b;
        color: white;
    }
    .btn-active-order:active{
        background-color: #76923b;
        color: white;
    }

    .btn-inactive-order{
       color: var(--card-heading-color);
       padding: 10px 1rem;
       border:none;
       background-color: transparent;
       font-size: 12px;
       width: 33%;
    }
    .btn-inactive-order:hover{
       color: var(--card-heading-color);
        border: none;
    }
    .btn-inactive-order:active{
       border: none;
       border-radius: 12px;
    }


    .orderl-list{
        overflow-y: auto;
        max-height: 400px;
        padding-right: 10px;
        padding-left: 10px;
    }

    .order-item{
        display: flex;
        align-items: start;
        justify-content: space-between;
    }

    
    .order-item{
        display: flex;
        align-items: start;
        margin-bottom: 10px;
        border-bottom: 1px dashed var(--order-background-color);
        padding: 10px 0;
    }

    .order-item:last-child{
        border-bottom: none;
        margin-bottom: 0;
    }

    .delhivery-time{
        font-size: 9px;
        width: 100%;
        
    }
    .item-small-hd{
        font-size: 13px;
        margin-bottom: 3px;
        font-weight: 500;
        line-height: 20px;
    }

    .item-price{
        margin-bottom: 10px;
        color: var(--dark-brown-color);
    }

    .item-price span {
    font-weight: 400;
    margin-right: 8px;
    font-size: 13px;
    }

    .item-action-cart{
        position: relative;
        bottom:0
    }

    .item-action-cart a, .item-action-cart p {
        background-color: white !important;
        color: var(--order-background-color) !important;
        border-color: var(--order-background-color);
        border-top: 1px solid;
        border-bottom: 1px solid;
    }
    .item-action-cart .add {
        border-right: 1px solid var(--order-background-color);
    }

    .item-action-cart .subtract {
        border-left: 1px solid var(--order-background-color);
    }

    .order-desscription{
        padding-right: 10px;
        margin-bottom: 0.5rem;
    }
    .final-subtotal{
        color: var(--order-background-color);
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
        font-weight: 600;
    }



    /* category */
    .category-item{
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        color: var(--card-heading-color);
        padding: 10px;
    }

    .category-item .order-count{
        font-weight: 600;
        color: var(--order-background-color);
    }
    .category-item .order-count p{
        margin-bottom: 0 ;
    }

    .category-item.active{
        background: linear-gradient(90deg, var(--order-background-color) 0%, #ffffff 100%);
        color: white;
        border-left: 3px solid #364e08;
    }







    /* .modal-food-item{
        max-width: 300px;
    } */

    .modal-food-item .modal-content{
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
    }
    .modal-food-item .modal-body{
        background-color: var(--body-color);
        padding: 0;
    }

    .btn-close-modal{
        position:absolute;
        top: 30px;
        right: 30px;
        background-color: white;
        padding: 10px;
        border-radius: 30px;
    }

    .item-img{
        background-color: white;
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 20px;
        padding: 1rem;
    }

    .item-img h5{
       color: var(--order-background-color);
       font-size: 24px;
       font-weight: 700;
    }


    .item-img img{
        border-radius: 1rem;
        width:100%
    }

    .price-text{
        font-size: 20px;
        color:var(--card-heading-color);
    }
    .meal-category{
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        background-color: white
    }

    .extra-status{
        text-transform: uppercase;
        font-size: 1rem;
       
        color: var(--card-location-color);
    }

    .text-status{
        color: var(--card-heading-color);
    }
    .nutrients-facts{
        color: var(--dark-brown-color);
        font-size: 1rem ;
        font-weight: 700;
    }

    .meal-category-table table th{
        background-color: var(--dark-brown-color);
        color: white;
        text-align: center;
    }

    .meal-category-table table td{
        text-align: center;
    }

    .item-ippopup-action{
        position: relative;
        left: 0;
        bottom:0;
        transform: translate(0,0)
    }

    .item-ippopup-action a, .item-ippopup-action p{
       border-top: 1px solid var(--order-background-color) ;
       border-bottom:1px solid var(--order-background-color) ;
       background-color: white !important;
       color: var(--darkest-green-bg-color) !important;
       height:38px !important;

    }
    .item-ippopup-action .subtract{
       border-left: 1px solid var(--order-background-color) ;
       
    }

    .item-ippopup-action .add{
       border-right:1px solid var(--order-background-color) ;
    }


    .modal-search-dish{

    }

    .search-item-list{
        width:100%;
        border-bottom: 0;
    }

    .search-item-list li{
        border-bottom: 1px dashed var(--card-location-color);
        width: 100%;
    }

    .search-item-list li:last-child{
        border: none;
    }

    .modal-search-dish .bg-modal-body-color {
        background-color: var(--body-color) ;
    }

    .searchitem-dish-image{
        width: 100px;
        height: 70px;
        object-fit: cover;
        border-radius: 10px;
    }

    .searchitem-dish-name{
        font-size: 1rem;
        color: var(--card-heading-color);
        padding-left: 1rem;
    }

    .mobile-cart{
        display: none;
    }

    .view-cart-mobile{
        display: flex;
        font-size: 18px;
        align-items: center;
        font-weight: 700;
        justify-content: space-between;
    }


    @media screen and (max-width:991.91px) {
        .mobile-cart{
            display: block;
            position: fixed;
            bottom: 30px;
            z-index:99;
            padding: 10px;
            width: 100%;
        }

        .mobile-cart button{
            width: calc(100vw - 2rem);
            padding: 1rem;
        }

        .cart-desktop{
            display: none;
        }
    }

</style>