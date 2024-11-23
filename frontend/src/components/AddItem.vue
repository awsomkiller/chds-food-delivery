<template>

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

        <!-- extra customization -->
        <div class="px-3 py-2 extra-options">
            <div class="meal-category toggle-button-extra rounded p-3">
                <h4 class="extra-status"> Extra protein </h4>
                <div class="">
                    <div class="can-toggle">
                        <input id="a" type="checkbox">
                        <label for="a">
                            <div class="can-toggle__switch" data-checked="Yes" data-unchecked="No"></div>
                        </label>
                    </div>
                </div>
            </div>

            <div class="meal-category toggle-button-extra rounded p-3">
                <h4 class="extra-status"> Extra vegetables </h4>
                <div class="meal-category toggle-button-extra rounded ">
                    <div class="">
                        <div class="can-toggle">
                            <input id="a" type="checkbox">
                            <label for="a">
                                <div class="can-toggle__switch" data-checked="Yes" data-unchecked="No"></div>
                            </label>
                        </div>
                    </div>
                </div>
            </div>


            <div class="meal-category toggle-button-extra rounded p-3">
                <h4 class="extra-status"> Extra rice  </h4>
                <div class=" toggle-button-extra rounded ">
                    <div class="">
                        <div class="can-toggle">
                            <input id="a" type="checkbox">
                            <label for="a">
                                <div class="can-toggle__switch" data-checked="Yes" data-unchecked="No"></div>
                            </label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
       

        <div class="px-3 py-2 pt-4">
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


</template>