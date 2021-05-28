<template>
  <div class="error-bg-color">
    <div class="error-contnet-position">
      <h1 class="mb-10" style="color: #696969">
        <slot name="title">
        </slot>
      </h1>
      <div>
        <slot name="content">
        </slot>
      </div>
    </div>
  </div>
</template>

<style>
.error-bg-color {
  height: 100%;
  background-color: #e9f4f6 !important;
}
.error-contnet-position {
  position: absolute;
  top: 50px;
  left: 50px;
}
.error-btn-bgcolor {
  background-color: white;
}
</style>