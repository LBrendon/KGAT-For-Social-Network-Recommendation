import argparse


def parse_ecfkg_args():
    parser = argparse.ArgumentParser(description="Run ECFKG.")

    parser.add_argument('--seed', type=int, default=2019,
                        help='Random seed.')

    parser.add_argument('--data_name', nargs='?', default='output',
                        help='Choose a dataset from {yelp2018, last-fm, amazon-book}')
    parser.add_argument('--data_dir', nargs='?', default='G:/5P30/FinalProject/KGAT-pytorch-master/kg_generate/datasets/facebook',
                        help='Input data path.')

    parser.add_argument('--use_pretrain', type=int, default=0,
                        help='0: No pretrain, 1: Pretrain with the learned embeddings, 2: Pretrain with stored model.')
    parser.add_argument('--pretrain_embedding_dir', nargs='?', default='datasets/pretrain/',
                        help='Path of learned embeddings.')
    parser.add_argument('--pretrain_model_path', nargs='?', default='trained_model/model.pth',
                        help='Path of stored model.')

    parser.add_argument('--embed_dim', type=int, default=64,
                        help='User / entity / relation Embedding size.')

    parser.add_argument('--train_batch_size', type=int, default=2048,
                        help='KG batch size.')
    parser.add_argument('--test_batch_size', type=int, default=10000,
                        help='Test batch size (the user number to test every batch).')

    parser.add_argument('--lr', type=float, default=0.0001,
                        help='Learning rate.')
    parser.add_argument('--n_epoch', type=int, default=100,
                        help='Number of epoch.')
    parser.add_argument('--stopping_steps', type=int, default=10,
                        help='Number of epoch for early stopping')

    parser.add_argument('--print_every', type=int, default=1,
                        help='Iter interval of printing loss.')
    parser.add_argument('--evaluate_every', type=int, default=10,
                        help='Epoch interval of evaluating CF.')

    parser.add_argument('--Ks', nargs='?', default='[20, 40, 60, 80, 100]',
                        help='Calculate metric@K when evaluating.')

    args = parser.parse_args()

    save_dir = 'trained_model/ECFKG/{}/embed-dim{}_lr{}_pretrain{}/'.format(
        args.data_name, args.embed_dim, args.lr, args.use_pretrain)
    args.save_dir = save_dir

    return args


