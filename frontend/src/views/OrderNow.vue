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
            <div class="col-lg-8 col-md-12 col-sm-12 col-12 p-3">
                <div class="menu-items">
                    <div class="row ">
                        <div class="col-lg-6 col-md-12 col-sm-12 col-12 p-0 pe-1">
                            <div class="outlet-card p-2">
                                <div class="restaurent-img">
                                <img class="" src="../assets/CHDS logo Blk transparent.png"> 
                                </div>
                                <div class="outlet-detail">
                                    <h5> Chi Hun Da Su </h5>
                                    <p> Location </p>
                                </div>
                            </div>
                            
                        </div>

                        <div class="col-lg-6 col-md-12 col-sm-12 col-12 p-0 ps-1">
                            <div class="search-filter h-100 p-2">
                                <form class="d-flex" role="search">
                                    <input class="form-control me-2" type="search" placeholder="Search menu" aria-label="Search">
                                    <button class="btn btn-outline-success" type="submit"><i class="fa-solid fa-magnifying-glass"></i></button>
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
                        <div class="col-md-6 col-sm-12 col-12 p-2">
                            
                            <div class="card-item " type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                <div class="card-item-food p-3">
                                    <div class="food-item-detail">
                                        <h5> Wine-Marinated Chicken Hearts </h5>
                                        <p class="item-price"> <small>$ 124 </small> $80 </p>
                                        <p class="item-description">
                                            Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as…
                                        </p>
                                    </div>
                                    <div class="food-image-n-add-item">
                                        <img class="" src="../assets/dish-images/Soy Braised Beef Shank.png">
                                        <a href="" class="add-item-action">
                                            Add +
                                        </a>
                                    </div>
                                    
                                </div>

                                <div class="calories-detail">
                                    <span class="overall-cal"> 800 Kcal</span>
                                    <ul class="list-unstyled ingridients-list">
                                        <li> 
                                            <span class="nutreents" >Protein </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Carbes </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Fat </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Neutrients </span>
                                            <span> 200g </span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            
                        </div>

                        <div class="col-md-6 col-sm-12 col-12 p-2">
                            
                            <div class="card-item ">
                                <div class="card-item-food p-3">
                                    <div class="food-item-detail">
                                        <h5> Wine-Marinated Chicken Hearts </h5>
                                        <p class="item-price"> <small>$ 124 </small> $80 </p>
                                        <p class="item-description">
                                            Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as…
                                        </p>
                                    </div>
                                    <div class="food-image-n-add-item">
                                        <img class="" src="../assets/dish-images/Soy Braised Beef Shank(1).png">
                                        <a href="" class="add-item-action">
                                            Add +
                                        </a>
                                    </div>
                                    
                                </div>

                                <div class="calories-detail">
                                    <span class="overall-cal"> 800 Kcal</span>
                                    <ul class="list-unstyled ingridients-list">
                                        <li> 
                                            <span class="nutreents" >Protein </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Carbes </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Fat </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Neutrients </span>
                                            <span> 200g </span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            
                        </div>

                        <div class="col-md-6 col-sm-12 col-12 p-2">
                            
                            <div class="card-item ">
                                <div class="card-item-food p-3">
                                    <div class="food-item-detail">
                                        <h5> Wine-Marinated Chicken Hearts </h5>
                                        <p class="item-price"> <small>$ 124 </small> $80 </p>
                                        <p class="item-description">
                                            Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as…
                                        </p>
                                    </div>
                                    <div class="food-image-n-add-item">
                                        <img class="" src="../assets/dish-images/Pickled Veg Chicken Stir-fry.png">
                                        <a href="" class="add-item-action">
                                            Add +
                                        </a>
                                    </div>
                                    
                                </div>

                                <div class="calories-detail">
                                    <span class="overall-cal"> 800 Kcal</span>
                                    <ul class="list-unstyled ingridients-list">
                                        <li> 
                                            <span class="nutreents" >Protein </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Carbes </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Fat </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Neutrients </span>
                                            <span> 200g </span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            
                        </div>

                        <div class="col-md-6 col-sm-12 col-12 p-2">
                            
                            <div class="card-item ">
                                <div class="card-item-food p-3">
                                    <div class="food-item-detail">
                                        <h5> Wine-Marinated Chicken Hearts </h5>
                                        <p class="item-price"> <small>$ 124 </small> $80 </p>
                                        <p class="item-description">
                                            Tender chicken hearts marinated in wine sauce, offering a rich and unique flavor, perfect as…
                                        </p>
                                    </div>
                                    <div class="food-image-n-add-item">
                                        <img class="" src="../assets/dish-images/Pickled Veg Chicken Stir-fry(1).png">
                                        <div class="item-action">
                                            <a href="" class="subtract">
                                                <i class="fa-solid fa-minus"></i>
                                            </a>
                                            <p>20</p>
                                            <a href="" class="add">
                                                <i class="fa-solid fa-plus"></i>
                                            </a>
                                        </div>
                                        
                                    </div>
                                    
                                </div>

                                <div class="calories-detail">
                                    <span class="overall-cal"> 800 Kcal</span>
                                    <ul class="list-unstyled ingridients-list">
                                        <li> 
                                            <span class="nutreents" >Protein </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Carbes </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Fat </span>
                                            <span> 200g </span>
                                        </li>

                                        <li> 
                                            <span  class="nutreents">Neutrients </span>
                                            <span> 200g </span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                    
                </div>
            </div>


            <!-- cart  -->
            <div class="col-lg-4 col-md-12 col-sm-12 col-12 p-2">
                <div class="bg-white cart-section p-2 rounded ">
                    <div class="pb-3">
                        <h4 class="cart-heading"> Your Cart</h4>
                    
                        <div class="order-type-container">
                            <button type="button" class="btn-active-order"> <span> Delivery </span> <br> <span class="delhivery-time">20 Minutes</span> </button>
                            <button type="button" class="btn-inactive-order">Pick Up</button>
                            <button type="button" class="btn-inactive-order">In Car</button>
                        </div>
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
                        <div class="final-subtotal">
                            <span>Subtotal </span>
                            <span> $  800.00</span>
                        </div>
                        <div class="final-subtotal fw-normal">
                            <span class=" ">Delivery Charges </span>
                            <span> $  20.00</span>
                        </div>

                        <button type="button" class="btn btn-primary w-100"> Checkout $ 820.00 </button>
                    </div>
                    
                </div>
            </div>
        </div>
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

            <div class="price-text"> $ <span class="fw-bold">399 </span> </div>
        </div>
        </div>
        

        <div class="meal-category p-3">
            <input type="radio" class="btn-check " name="options" id="option1" autocomplete="off" checked>
            <label class="btn btn-primary" for="option1">Meal Set</label>

            <input type="radio" class="btn-check" name="options" id="option2" autocomplete="off">
            <label class="btn btn-outline-primary" for="option2"> Main Dish (300 g)</label>

           
            
        </div>


        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary">Add to Cart</button>
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
        
        --order-background-color: #76923b;

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
        top: -1.25rem;
        left: 50px;
        right: 0;
        color: var(--card-heading-color);
        background-color: var(--body-color) !important;
        width: max-content;
        padding: 0 10px;
    }


    .card-item {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 0px 8px rgb(0 0 0 / 10%);
    }

    .card-item-food{
        display: flex;
        
    }
    .food-item-detail{
        flex: 0 0 60%;
        padding-right: 0.5rem;
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
        border-radius: 6px;
        height: 135px;
        width: 135px;
        object-fit: cover;
        
    }

    .add-item-action{
        font-size: 16px;
        font-weight: 600;
        padding: 3px 12px;
        border: 1px solid var(--card-heading-color);
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
        color: #333333
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
        margin-bottom: 0px;
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
    .item-img img{
        border-radius: 30px;
        width:100%
    }

    .price-text{
        font-size: 20px;
        color:var(--card-heading-color)
    }
    .meal-category{
        display: flex;
        gap: 1rem;
    }
</style>