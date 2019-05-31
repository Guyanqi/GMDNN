python train.py \
 --save_weights_path="weights/ex1/"  \
 --train_images="dataset1/images_prepped_train/" \
 --train_annotations="dataset1/annotations_prepped_train/" \
 --val_images="dataset1/images_prepped_test/" \
 --val_annotations="dataset1/annotations_prepped_test/" \
 --n_classes=50  \
 --input_height=320 \
 --input_width=640 \
 --model_name="segnet_res_crf"